# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    # 可以根据时间段，以及桌号对订单进行过滤
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

    # 重写retrieve方法。在返回响应之前，检查Order对象是否有相关的DishDetail对象，如果有，就更新total_amount
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if instance.dishdetail_set.exists():
    #         instance.total_amount = sum(detail.total_price for detail in instance.dishdetail_set.all())
    #         instance.save()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


# 菜品详情表视图
class DishDetailViewSet(viewsets.ModelViewSet):
    queryset = DishDetail.objects.all().order_by('id')
    serializer_class = DishDetailSerializer
    # permission_classes = [IsAuthenticated]
