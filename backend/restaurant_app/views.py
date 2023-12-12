# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Table, DishCategory, DishUnit, Dish, Order, DishDetail
from .serializers import TableSerializer, DishCategorySerializer, DishUnitSerializer, DishSerializer, OrderSerializer, \
    DishDetailSerializer


# 桌位表视图
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    # permission_classes = [IsAuthenticated]


# 菜品分类表视图
class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    # permission_classes = [IsAuthenticated]


# 菜品单位表视图
class DishUnitViewSet(viewsets.ModelViewSet):
    queryset = DishUnit.objects.all()
    serializer_class = DishUnitSerializer
    # permission_classes = [IsAuthenticated]


# 菜品表视图
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    # permission_classes = [IsAuthenticated]


# 订单表视图
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]


# 菜品详情表视图
class DishDetailViewSet(viewsets.ModelViewSet):
    queryset = DishDetail.objects.all()
    serializer_class = DishDetailSerializer
    # permission_classes = [IsAuthenticated]
