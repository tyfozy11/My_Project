from django.contrib.auth.models import AbstractUser
from django.db import models


def dish_upload_path(obj, file):
    return f'product/{obj.id}/{file}'


class CoreUser(AbstractUser):
    address = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=10, default='')


class Name(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Orders(models.Model):
    buyer_address = models.ForeignKey("core.CoreUser", on_delete=models.SET_NULL, null=True, related_name='buyer_address')
    buyer_phone = models.ForeignKey("core.CoreUser", on_delete=models.SET_NULL, null=True, related_name='buyer_phone')
    buyer_name = models.ForeignKey("core.CoreUser", on_delete=models.SET_NULL, null=True, related_name='buyer_name')
    comments = models.TextField()


class Dish(Name):
    category = models.ForeignKey("core.FoodCategories", on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    core_image = models.ImageField(upload_to=dish_upload_path)


class Images(Name):
    dish = models.ForeignKey("core.Dish", on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=dish_upload_path)


class FoodCategories(Name):
    image = models.ImageField(blank=True, null=True, upload_to=dish_upload_path)


class Basket(models.Model):
    product = models.ManyToManyField("core.Dish")
    sum_prices = models.DecimalField(max_digits=6, decimal_places=2)
    profile = models.ForeignKey("core.CoreUser", on_delete=models.SET_NULL, null=True)
