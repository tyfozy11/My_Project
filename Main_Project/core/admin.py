from django.contrib import admin
from core import models


class OrderStatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.CoreUser)
admin.site.register(models.FoodCategories)
admin.site.register(models.Dish)
