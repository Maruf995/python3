import requests
from django.http import HttpResponseRedirect

from . import forms
from django.shortcuts import render
from django.views.generic import ListView, FormView
from . import models

class FilmView(ListView):
    model = models.Film
    template_name = 'films/films_list.html'

    def get_queryset(self):
        return models.Film.objects.all()

class ParserFilmView(FormView):
    template_name = 'films/films_parser.html'
    form_class = forms.ParserForm
    success_url = '/films'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserFilmView, self).post(request, *args, **kwargs)