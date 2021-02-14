from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import UserProfile, Admin
from users.permissions import AdminPermission, UserPermission
from users.serializers import UserProfileSerializer, AdminSerializer, \
    UserSerializer


class AdminViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, AdminPermission)
    serializer_class = AdminSerializer
    queryset = Admin.objects.all().order_by('-created')

    """
        Create user account in auth_user table for authenticate. 
        Insert custom email for prevent duplicate authentication. 
    """
    def create(self, request, *args, **kwargs):
        request.data['email'] = f"{request.data.get('username', None)}" \
                                f"@promo.com"
        request.data['is_superuser'] = True
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        request.data['user'] = user_serializer.data['id']
        user_profile_serializer = self.serializer_class(data=request.data)
        user_profile_serializer.is_valid(raise_exception=True)
        user_profile_serializer.save()
        return Response(user_profile_serializer.data,
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        admin = get_object_or_404(Admin, uuid=kwargs['pk'])
        User.objects.filter(pk=admin.user.pk).delete()
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, UserPermission)
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all().order_by('-created')

    """ 
        Create user account in auth_user table for authenticate. 
        Insert custom email for prevent duplicate authentication. 
    """
    def create(self, request, *args, **kwargs):
        request.data['email'] = f"{request.data.get('username', None)}" \
                                f"@promo.com"
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        request.data['user'] = user_serializer.data['id']
        user_profile_serializer = self.serializer_class(data=request.data)
        user_profile_serializer.is_valid(raise_exception=True)
        user_profile_serializer.save()
        return Response(user_profile_serializer.data,
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, uuid=kwargs['pk'])
        User.objects.filter(pk=user_profile.user.pk).delete()
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
