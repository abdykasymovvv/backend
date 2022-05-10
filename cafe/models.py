import datetime
from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    """ Столы """
    chair = models.IntegerField()
    Status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'


class Eat(models.Model):
    """ Еда """
    NameFood = models.CharField(max_length=50)
    description = models.TextField('Описание', max_length=150)
    Price = models.IntegerField()

    def __str__(self):
        return self.NameFood

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'


class PreOrder(models.Model):
    """ Предзаказ """
    eat = models.ManyToManyField(Eat, related_name="preorder")
    time = models.DateTimeField(auto_now=datetime.datetime.now())
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="table")
    customer = models.ForeignKey(User, related_name='customerPreOrder', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Предзаказ'
        verbose_name_plural = 'Предзаказы'


class OrderHome(models.Model):
    """ Заказ на дом """
    eat = models.ManyToManyField(Eat, related_name="orderhome")
    time = models.DateTimeField(auto_now=datetime.datetime.now())
    street = models.CharField(max_length=50)
    customer = models.ForeignKey(User, related_name='customerOrderHome', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'