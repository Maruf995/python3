from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .models import BlogPost
from post.models import BlogPost

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
    return render(request, "blog_detail.html", context={"post": post})

class CreateBlogView(CreateView):
    model = BlogPost
    template_name = "blog_form.html"
    fields = [
        "image",
        "title",
        "description",
    ]