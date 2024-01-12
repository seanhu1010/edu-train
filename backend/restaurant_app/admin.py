from django.contrib import admin
from .models import Table, DishCategory, DishUnit, DishImage, Dish, Order, DishDetail

# Register your models here.

admin.site.register(Table)
admin.site.register(DishCategory)
admin.site.register(DishUnit)
admin.site.register(DishImage)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(DishDetail)
