from rest_framework.serializers import ModelSerializer
from .models import User

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'age', 'working_hours')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_yosh(self, value):
        if value < 16:
            raise serializers.ValidationError("Yoshingiz mos kelmaydi")
        return value


class AdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'age', 'working_hours')
        extra_kwargs = {'password': {'write_only': True}}


