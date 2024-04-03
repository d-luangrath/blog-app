from django.shortcuts import render
from app.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'app/index.html', context)

def post_page(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        context = {"slug": slug}
        return render(request, 'app/not_found.html', context)

    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count += 1
    post.save()
    
    context = {'post': post}
    return render(request, 'app/post.html', context)