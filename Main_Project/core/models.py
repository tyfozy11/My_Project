from django.contrib.auth.models import AbstractUser
from django.db import models


def dish_upload_path(obj, file):
    return f'product/{obj.id}/{file}'


class CoreUser(AbstractUser):
    pass


class Name(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Dish(Name):
    category = models.ForeignKey("core.FoodCategories", on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to=dish_upload_path)


class FoodCategories(Name):
    pass
