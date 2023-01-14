"""Main_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("profile/", views.ProfileView.as_view(template_name='profile.html'), name='profile'),
                  path("search/", views.SearchView.as_view(template_name='search.html'), name='search'),
                  path("basket/", views.BasketView.as_view(template_name='basket.html'), name='basket'),
                  path("", views.IndexView.as_view(template_name='home.html'), name='home'),
                  path("registration/", views.RegistrationView.as_view(template_name='registration.html'), name='registration'),
                  path("login/", LoginView.as_view(template_name='login.html'), name='login'),
                  path("logout/", LogoutView.as_view(template_name='login.html'), name='logout'),
                  path("dishes/", views.DishView.as_view(template_name='dishes.html'), name='dishes'),
                  path("dishes_from/<int:category_id>/category/", views.DishFromCategoryView.as_view(template_name='dishes_from_category.html'), name='dishes_from_category'),
                  path("categories/", views.FoodCategoriesView.as_view(template_name='categories.html'), name='categories'),
                  path('__debug__/', include('debug_toolbar.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)