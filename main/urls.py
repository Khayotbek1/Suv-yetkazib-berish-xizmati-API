from django.urls import path
from main.views import *

urlpatterns = [
    path('waters/', WaterListCreateView.as_view()),
    path('water/', WaterRetrieveUpdateDestroyView.as_view()),
    path('clients/', ClientListCreateView.as_view()),
    path('client/', ClientRetrieveUpdateDestroyView.as_view()),
    path('orders/', OrderListCreateView.as_view()),
    path('drivers/', DriverListAPIView.as_view()),
    path('driver/', DriverRetrieveAPIView.as_view()),

]