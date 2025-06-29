from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class RegisterUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def get_object(self):
        return self.request.user

class AdminListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (IsAuthenticated,)


class AdminRetrieAPIView(RetrieveAPIView):
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        return self.request.user