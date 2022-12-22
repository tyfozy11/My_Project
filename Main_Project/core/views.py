from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import UpdateView, ListView, FormView, TemplateView
from core.models import FoodCategories, Dish


class IndexView(TemplateView):
    template_name = 'home.html'
    model = FoodCategories


class ProfileView(TemplateView):
    template_name = 'profile.html'


class DishView(ListView):
    template_name = 'dishes.html'
    model = Dish
    paginate_by = 10

    # def get_queryset(self):
    #     queryset = super(DishView, self).get_queryset()
    #     return queryset
