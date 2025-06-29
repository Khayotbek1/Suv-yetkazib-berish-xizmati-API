from rest_framework.generics import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

class WaterListCreateView(ListCreateAPIView):
    queryset = Water.objects.all()
    serializer_class = WaterSerializer
    permission_classes = [IsAuthenticated]


class WaterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = WaterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Water.objects.filter(user=self.request.user)


class ClientListCreateView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'phone_number']

class ClientRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['water', 'client']
    ordering_fields = ['created_at']


class DriverListAPIView(ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]


class DriverRetrieveAPIView(RetrieveAPIView):
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Driver.objects.filter(user=self.request.user)







