from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView, TemplateView, UpdateView
from core.models import FoodCategories, Dish, Images
from core.forms import RegistrationForm, EditUserForm


class IndexView(ListView):
    model = Dish
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        if 'refresh_count' not in self.request.session:
            self.request.session['refresh_count'] = 0

        self.request.session['refresh_count'] += 1
        context['refresh_count'] = self.request.session['refresh_count']
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class ProductDetailView(DetailView):
    model = Images
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super(ProductDetailView, self).get_queryset()
        queryset = Dish.objects.filter(id=self.kwargs['id'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context.update({
            'images': Images.objects.filter(dish_id=self.kwargs['id'])
        })
        return context


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
    paginate_by = 9

    def get_queryset(self):
        queryset = super(DishFromCategoryView, self).get_queryset()
        queryset = Dish.objects.filter(category=self.kwargs['category_id'])
        return queryset.order_by('price')


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
            return self.model.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            ).order_by('name')

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


class EditUserView(UpdateView):
    template_name = 'edit_user.html'
    model = get_user_model()
    form_class = EditUserForm
    pk_url_kwarg = 'user_id'
    success_url = '/'


class BasketView(FormView):
    template_name = 'basket.html'
