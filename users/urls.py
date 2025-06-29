from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from .views import *

urlpatterns = [
    path('token/', token_obtain_pair, name='token'),
    path('token/refresh/', token_refresh, name='token-refresh'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('admins/', AdminListAPIView.as_view(), name='admins'),
    path('admin/me/', AdminRetrieAPIView.as_view(), name='admin-me'),

]