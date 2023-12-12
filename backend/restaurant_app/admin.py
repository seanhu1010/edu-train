from django.contrib import admin
from .models import Table, DishCategory, DishUnit, Dish, Order, DishDetail

# Register your models here.

admin.site.register(Table)
admin.site.register(DishCategory)
admin.site.register(DishUnit)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(DishDetail)
