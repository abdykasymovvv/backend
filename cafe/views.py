from . serializer import EatCreateSerializer, TableSerializer, PreOrderSerializer, OrderHomeSerializer
from .models import Eat, Table, OrderHome, PreOrder
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class EatCreate(generics.CreateAPIView):
    queryset = Eat.objects.all()
    serializer_class = EatCreateSerializer
    permission_classes = [IsAdminUser, ]


class EatList(generics.ListAPIView):
    queryset = Eat.objects.all()
    serializer_class = EatCreateSerializer


class EatUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eat.objects.all()
    serializer_class = EatCreateSerializer
    permission_classes = [IsAuthenticated]


class TableListCreate(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]


class TableUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderHomeListCreate(generics.ListCreateAPIView):
    queryset = OrderHome.objects.all()
    serializer_class = OrderHomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return OrderHome.objects.filter(customer=user)


class OrderHomeUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderHome.objects.all()
    serializer_class = OrderHomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return OrderHome.objects.filter(customer=user)


class PreOrderListCreate(generics.ListCreateAPIView):
    queryset = PreOrder.objects.all()
    serializer_class = PreOrderSerializer
    permission_classes = [IsAuthenticated, ]


class PreOrderUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PreOrder.objects.all()
    serializer_class = PreOrderSerializer
    permission_classes = [IsAuthenticated, ]