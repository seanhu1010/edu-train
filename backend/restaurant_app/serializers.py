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
    transaction_time = serializers.SerializerMethodField()
    dish_details = serializers.SerializerMethodField()  # 新增字段

    class Meta:
        model = Order
        fields = '__all__'

    def get_transaction_time(self, obj):
        return obj.transaction_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_dish_details(self, obj):
        dish_details = DishDetail.objects.filter(order=obj)
        return DishDetailSerializer(dish_details, many=True).data


# 菜品详情表序列化
class DishDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()  # 菜品名称
    unit = serializers.SerializerMethodField()  # 菜品单位
    specification = serializers.SerializerMethodField()  # 菜品规格

    class Meta:
        model = DishDetail
        fields = '__all__'

    def get_name(self, obj):
        return obj.dish.name

    def get_unit(self, obj):
        return obj.dish.unit.unit

    def get_specification(self, obj):
        return obj.dish.specification