from django.shortcuts import render
from django.views.generic import UpdateView, ListView, FormView, TemplateView
from core.models import FoodCategories


class IndexView(TemplateView):
    template_name = 'home.html'
    models = FoodCategories
