from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from .models import BlogPost
from post.models import BlogPost, Comment

def hello_world_view(request):
    return HttpResponse("Hello, World!")


def date_view(request):
    now = datetime.now()
    return HttpResponse(str(now))


def blog_view(request):
    posts: list = BlogPost.objects.all()
    return render(request, "blog.html", context={"posts": posts})


def post_detail(request, pk):
    post: BlogPost = BlogPost.objects.get(pk=pk)
    comments = Comment.objects.filter(pk=pk).order_by("-date")
    return render(request, "blog_detail.html", context={"post": post})

class CreateBlogView(CreateView):
    model = BlogPost
    template_name = "blog_form.html"
    fields = [
        "image",
        "title",
        "description",
    ]

def create_comment(request, pk):
    if request.method == "POST":
        data: dict = request.POST
        post = BlogPost.objetcs.get(pk=pk)
        comment = Comment.objetcs.create(text=data["text"], post=post)
        return redirect("blog-detail")


class EditBlogView(UpdateView):
    model = BlogPost
    template_name = "edit.html"
    fields = {
        "title",
        "description",
        "image"
    }


