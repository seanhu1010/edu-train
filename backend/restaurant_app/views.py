# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Table, DishCategory, DishUnit, Dish, Order, DishDetail
from .serializers import TableSerializer, DishCategorySerializer, DishUnitSerializer, DishSerializer, OrderSerializer, \
    DishDetailSerializer


# 桌位表视图
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('table_number')
    serializer_class = TableSerializer
    pagination_class = None
    # permission_classes = [IsAuthenticated]


# 菜品分类表视图
class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all().order_by('id')
    serializer_class = DishCategorySerializer
    # permission_classes = [IsAuthenticated]


# 菜品单位表视图
class DishUnitViewSet(viewsets.ModelViewSet):
    queryset = DishUnit.objects.all().order_by('id')
    serializer_class = DishUnitSerializer
    # permission_classes = [IsAuthenticated]


# 菜品表视图
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all().order_by('id')
    serializer_class = DishSerializer
    # permission_classes = [IsAuthenticated]


# 订单表视图
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-transaction_time')
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)
        table_number = self.request.query_params.get('table_number', None)

        if start_time is not None and end_time is not None:
            queryset = queryset.filter(transaction_time__range=[start_time, end_time])

        if table_number is not None:
            queryset = queryset.filter(table__table_number=table_number)

        return queryset.order_by('-transaction_time')


# 菜品详情表视图
class DishDetailViewSet(viewsets.ModelViewSet):
    queryset = DishDetail.objects.all().order_by('id')
    serializer_class = DishDetailSerializer
    # permission_classes = [IsAuthenticated]
