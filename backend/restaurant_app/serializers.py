# serializers.py
from rest_framework import serializers
from .models import Table, DishCategory, DishUnit, Dish, Order, DishDetail


# 桌位表序列化
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


# 菜品分类表序列化
class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory
        fields = '__all__'


# 菜品单位表序列化
class DishUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishUnit
        fields = '__all__'


# 菜品表序列化
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


# 订单表序列化
class OrderSerializer(serializers.ModelSerializer):
    dish_details = serializers.SerializerMethodField()  # 新增字段

    class Meta:
        model = Order
        fields = '__all__'

    def get_dish_details(self, obj):
        dish_details = DishDetail.objects.filter(order=obj)
        return DishDetailSerializer(dish_details, many=True).data


# 菜品详情表序列化
class DishDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishDetail
        fields = '__all__'
