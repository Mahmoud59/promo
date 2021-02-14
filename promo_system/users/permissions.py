from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from users.models import UserProfile


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.uuid == get_object_or_404(
            UserProfile, user=request.user.id).uuid
