from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from . import models, forms
from .forms import CommentForm
from .models import Comment, Books


class BookListView(ListView):
    template_name = 'books/book_list.html'
    queryset = models.Books.objects.all()

    def get_queryset(self):
        return models.Books.objects.all()

class BookCreateView(CreateView):
    template_name = 'books/book_create.html'
    form_class = forms.BookForm
    success_url = '/'
    queryset = models.Books.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)


class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

    def get_context_data(self, **kwargs):
        context: dict = super(BookDetailView, self).get_context_data(**kwargs)
        id = self.kwargs.get("id")
        comments: list[Comment] = Comment.objects.filter(comment_id=id).order_by("created_date")
        context["comments"] = comments
        return context

class BookUpdateView(UpdateView):
    template_name = 'books/book_create.html'
    form_class = forms.BookForm

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('books:book-list')


class BookDeleteView(DeleteView):
    template_name = 'books/book_delete.html'

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

    def get_success_url(self):
        return reverse('books:book-list')

def create_comment(request, id):
    if request.method == "POST":
        data: dict = request.POST
        id_ = id
        if data.get("text"):
            Comment.objects.create(text=data["text"], comment_id=id_)
            return redirect(f'/{id_}/')
        else:
            return HttpResponse("field is empty!!!")