from django.shortcuts import render, redirect, get_object_or_404
from app.models import Post, Comments,Tag, Profile, WebsiteMeta
from app.forms import CommentForm, SubscribeForm, NewUserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth import login

# Create your views here.
def index(request):
    posts = Post.objects.all()
    top_posts = Post.objects.all().order_by('-view_count')[0:3]
    recent_posts = Post.objects.all().order_by('-last_updated')[0:3]
    featured_blog = Post.objects.filter(is_featured=True)
    subscribe_form = SubscribeForm()
    success = None
    website_info = None

    if WebsiteMeta.objects.all().exists():
        website_info = WebsiteMeta.objects.all()[0]

    if featured_blog:
        featured_blog = featured_blog[0]

    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            request.session['subscribed'] = True
            success = "Subscribed Successfully"
            subscribe_form = SubscribeForm()

    context = {
        "posts": posts,
        "top_posts": top_posts,
        "recent_posts": recent_posts,
        "subscribe_form": subscribe_form,
        "success": success,
        "featured_blog": featured_blog,
        "website_info": website_info
    }
    
    return render(request, "app/index.html", context)


def post_page(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        context = {"slug": slug}
        return render(request, "app/not_found.html", context)

    post = Post.objects.get(slug=slug)
    comments = Comments.objects.filter(post=post, parent=None)
    form = CommentForm()

    # Bookmark logic
    bookmarked = False
    if post.bookmarks.filter(id = request.user.id).exists():
        bookmarked = True
    is_bookmarked = bookmarked


    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            if parent := request.POST.get('parent'):
                # save reply
                if parent_comment := Comments.objects.get(id=parent):
                    comment_reply = comment_form.save(commit=False)
                    comment_reply.parent = parent_comment
                    comment_reply.post = post
                    comment_reply.save()
                    return HttpResponseRedirect(reverse('post_page', kwargs={'slug': slug}))
            else:
                comment = comment_form.save(commit=False)
                post_id = request.POST.get('post_id')
                post = Post.objects.get(id = post_id)
                comment.post = post
                comment.save()
                return HttpResponseRedirect(reverse('post_page', kwargs={'slug': slug}))

    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count += 1
    post.save()

    context = {
        "post": post,
        "form": form, 
        "comments": comments,
        "is_bookmarked": is_bookmarked
    }
    
    return render(request, "app/post.html", context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)

    top_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-view_count')[0:2]
    recent_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-last_updated')[0:2]

    tags = Tag.objects.all()
    context = {
        'tag': tag,
        'top_posts': top_posts,
        'recent_posts':recent_posts,
        'tags': tags
    }
    return render(request, 'app/tag.html', context)


def author_page(request, slug):
    profile = Profile.objects.get(slug=slug)

    top_posts = Post.objects.filter(author = profile.user).order_by('-view_count')[0:2]
    recent_posts = Post.objects.filter(author = profile.user).order_by('-last_updated')[0:2]
    top_authors = User.objects.annotate(number=Count('post')).order_by('number')

    context = {
        'profile': profile,
        'top_posts': top_posts,
        'recent_posts':recent_posts,
        'top_authors': top_authors
    }
    return render(request, 'app/author.html', context)


def search_posts(request):
    search_query = ""  # query entered in the search box
    if q := request.GET.get('q'):  # 'q' is the search query getting from request
        search_query = q  # store the query
    posts = Post.objects.filter(title__icontains=search_query)  # query the db to get all the post from the db
    context = {
        "posts": posts,
        "search_query_val": search_query
    }
    return render(request, 'app/search.html', context)


def about(request):
    website_info = None

    if WebsiteMeta.objects.all().exists():
        website_info = WebsiteMeta.objects.all()[0]
        
    context={
        "website_info": website_info,
    }
    return render(request, 'app/about.html', context)


def register_user(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    context = {"form": form}
    return render(request, 'registration/registration.html', context)


def bookmark_post(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return HttpResponseRedirect(reverse('post_page', args=[str(slug)]))


def health_check(request):
    return HttpResponse("ok")
