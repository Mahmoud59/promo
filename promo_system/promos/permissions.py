from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from users.models import UserProfile


class PromoPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_superuser and (view.action == 'create'
           or view.action == 'destroy'):
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if not request.user.is_superuser and obj.user == \
           get_object_or_404(UserProfile, user=request.user.id).pk:
            return False
        return True
