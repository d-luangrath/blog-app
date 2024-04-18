# Blog App

Note: This app is under active development :wink:

## Features
- The home page displays features of top and recent posts on the blog
- Post page with various elements such as tags, likes, comments, and bookmarking a particular post
- Comment system allows a user to leave a comment and reply to that particular comment
- Dedicated page for tags and authors
- Personalize experience based on user behavior
- Allow users to search on the website

## Todo
- [x] Build post tags
- [x] Authentication functionality of login, logout, signup and robust validation
- [ ] Bookmarking and "likes"
- [x] Personalize experience based on user behavior
- [x] Implement search across the website
- [ ] Terraform - Infrastructure as code (IaC) - configs to deploy to AWS
- [ ] Deploy to AWS from terminal
- [ ] Automated tests

## Technologies
- Python
- Django
- Docker
- AWS (ECS, RDS)
- Postgres

## Demo (reminder - development is in progress)
**Home page of blog post showing top and featured posts**

![Home Page](img/home.png)

![Home Page half](img/home-features.png)

**Post page displays the photo and blog post**
![Post page](img/blog-post.png)

**Comment on a blog post and reply**
![Post Page half](img/comment.png)

**Clicking on a tag of a post and navigating to posts assicated with the tag**
![Tag Page](img/tags.png)

## Running the app locally

### Prerequisites
- Docker
- `make` command

#### Steps
1. Clone the repo
1. Navigate to the repo directory
1. Run `make` or `make build` to build containers
1. Run `make up`
1. Run `make migrate`
1. Navigate to http://0.0.0.0:8000

#### Make Commands
```
make build          Build containers
make up             Start containers
make down           Stop local dev environment
make restart        Down and up. Restart all containers
make sh, shell      Open shell into the app container
make db-shell       Open shell into DB container
make test           Run tests inside the container
make logs           Output container logs
make migrations     Create DB migration files
make migrate        Applies the changes recorded in migration files to the DB
```

## Deployment
Currently deployed manually in AWS ECS. DB is an RDS service.
Automated deployment TBD after Terraform is implemented
