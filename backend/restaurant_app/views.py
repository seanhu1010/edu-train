# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_list_or_404

from .models import Table, DishCategory, DishUnit, DishImage, Dish, Order, DishDetail, Employee
from .serializers import TableSerializer, DishCategorySerializer, DishUnitSerializer, DishImageSerializer, \
    DishSerializer, OrderSerializer, DishDetailSerializer, EmployeeSerializer


# 桌位表视图
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('table_number')
    serializer_class = TableSerializer
    pagination_class = None  # 不分页
    # permission_classes = [IsAuthenticated]


# 菜品分类表视图
class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all().order_by('id')
    serializer_class = DishCategorySerializer
    pagination_class = None  # 不分页
    # permission_classes = [IsAuthenticated]


# 菜品单位表视图
class DishUnitViewSet(viewsets.ModelViewSet):
    queryset = DishUnit.objects.all().order_by('id')
    serializer_class = DishUnitSerializer
    pagination_class = None  # 不分页
    # permission_classes = [IsAuthenticated]


class DishImageViewSet(viewsets.ModelViewSet):
    queryset = DishImage.objects.all().order_by('-id')
    serializer_class = DishImageSerializer
    # permission_classes = [IsAuthenticated]


# 菜品表视图
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all().order_by('-id')
    serializer_class = DishSerializer
    # permission_classes = [IsAuthenticated]


# 订单表视图
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-transaction_time')
    serializer_class = OrderSerializer

    # permission_classes = [IsAuthenticated]

    # 可以根据时间段，以及桌号对订单进行过滤
    # 例如：/orders?start_time=2023-12-01T00:00:00Z&end_time=2023-12-31T23:59:59Z&table_number=1
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


# 员工表视图
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAuthenticated]

    # 通过发送一个POST请求到/employees/delete-multiple/来使用
    # 在请求的body中提供一个名为ids的数组，其中包含想要删除的所有员工的id
    @action(detail=False, methods=['post'], url_path='delete-multiple')
    def delete_multiple(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])
        if not ids:
            return Response({'msg': '没有提供要删除的员工ID。'}, status=400)
        employees = get_list_or_404(Employee, id__in=ids)
        for employee in employees:
            employee.delete()
        return Response({'status': 'success'})
