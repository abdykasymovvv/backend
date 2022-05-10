from rest_framework import serializers
from .models import Eat, Table, PreOrder, OrderHome


class EatCreateSerializer(serializers.ModelSerializer):
    """Еда"""

    class Meta:
        model = Eat
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    """Столы"""

    class Meta:
        model = Table
        fields = '__all__'


class PreOrderSerializer(serializers.ModelSerializer):
    """Предзаказ"""
    time = serializers.DateTimeField()
    eat = serializers.SlugRelatedField(many=True, slug_field='eat', queryset=Eat.objects.all())
    table = serializers.SlugRelatedField(many=True, slug_field='eat', queryset=Table.objects.all())

    class Meta:
        model = PreOrder
        fields = "__all__"


class OrderHomeSerializer(serializers.ModelSerializer):
    """Заказ на дом """
    time = serializers.DateTimeField()
    eat = serializers.SlugRelatedField(many=True, slug_field='eat', queryset=Eat.objects.all())
    street = serializers.CharField()

    class Meta:
        model = OrderHome
        fields = "__all__"
