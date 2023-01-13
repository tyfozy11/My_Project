from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import UpdateView, ListView, FormView, TemplateView
from core.models import FoodCategories, Dish
from core.forms import RegistrationForm


class IndexView(TemplateView):
    template_name = 'home.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'


class DishView(ListView):
    template_name = 'dishes.html'
    model = Dish
    paginate_by = 9

    def get_queryset(self):
        queryset = super(DishView, self).get_queryset()
        return queryset.order_by("price")


class DishFromCategoryView(ListView):
    template_name = 'dishes_from_category.html'
    model = FoodCategories
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DishFromCategoryView, self).get_context_data(**kwargs)

        return context


class FoodCategoriesView(ListView):
    template_name = 'categories.html'
    model = FoodCategories
    paginate_by = 10

    def get_queryset(self):
        queryset = super(FoodCategoriesView, self).get_queryset()
        return queryset.order_by("name")


class SearchView(IndexView):
    template_name = 'search.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query:
            return self.model.objects.get_prefetched().filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            ).order_by('price')

        return super(SearchView, self).get_queryset()


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user = authenticate(
            self.request,
            username=user.username,
            password=form.cleaned_data['password']
        )
        login(request=self.request, user=user)
        return super(RegistrationView, self).form_valid(form)
