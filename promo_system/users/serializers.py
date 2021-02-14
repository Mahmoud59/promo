from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import UserProfile, Admin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, password):
        """Hash the password correctly."""
        return make_password(password)


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        read_only_fields = ('uuid',)
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        read_only_fields = ('uuid',)
        fields = '__all__'
