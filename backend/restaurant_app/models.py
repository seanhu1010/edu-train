from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# 桌位表
class Table(models.Model):
    table_number = models.IntegerField(verbose_name='桌号')

    def __str__(self):
        return str(self.table_number)


# 菜品分类表
class DishCategory(models.Model):
    category = models.CharField(max_length=200, verbose_name='菜品类别')

    def __str__(self):
        return self.category


# 菜品单位表
class DishUnit(models.Model):
    unit = models.CharField(max_length=200, verbose_name='菜品单位')

    def __str__(self):
        return self.unit


# 菜品表
class Dish(models.Model):
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, verbose_name='菜品所属分类')
    specification = models.CharField(max_length=200, verbose_name='菜品规格')
    image = models.ImageField(upload_to='images/', verbose_name='菜品图片')
    name = models.CharField(max_length=200, verbose_name='菜品名称')
    unit = models.ForeignKey(DishUnit, on_delete=models.CASCADE, verbose_name='菜品单位')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='菜品单价')

    def __str__(self):
        return self.name


# 订单表
class Order(models.Model):
    transaction_time = models.DateTimeField(auto_now_add=True, verbose_name='交易时间')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='桌号')
    number_of_people = models.IntegerField(verbose_name='用餐人数')
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='交易金额', blank=True, null=True)
    transaction_status = models.CharField(max_length=200, verbose_name='交易状态')

    def __str__(self):
        return str(self.id)


# 菜品详情表
class DishDetail(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='菜品id')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='订单id')
    quantity = models.IntegerField(verbose_name='菜品下单数量')
    total_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='总价', blank=True, null=True)

    def __str__(self):
        return f'{self.dish.name} - {self.order.id}'


# 在保存DishDetail之前，计算total_price
@receiver(pre_save, sender=DishDetail)
def calculate_total_price(sender, instance, **kwargs):
    instance.total_price = instance.dish.price * instance.quantity


# 在保存Order之前，计算total_amount
@receiver(pre_save, sender=Order)
def calculate_total_amount(sender, instance, **kwargs):
    instance.total_amount = sum(detail.total_price for detail in instance.dishdetail_set.all())
