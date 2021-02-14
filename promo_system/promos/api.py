from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from promos.models import Promo
from promos.permissions import PromoPermission
from promos.serializers import PromoSerializer
from users.models import UserProfile
from users.permissions import UserPermission


class PromoViewSet(ModelViewSet):
    serializer_class = PromoSerializer
    permission_classes = (IsAuthenticated, PromoPermission)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            user_profile = get_object_or_404(
                UserProfile, user=self.request.user.id)
            return Promo.objects.filter(user=user_profile).order_by('-id')
        else:
            queryset = Promo.objects.all().order_by('-id')
        return queryset


class PromoPointAPIView(APIView):
    permission_classes = (IsAuthenticated, UserPermission)

    def post(self, request, promo_id):
        print(111111111111111111111111111)
        print(request.user)
        print(111111111111111111111111111)
        if not request.data.get('amount', None):
            return Response({'message': "You must insert your amount."},
                            status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(UserProfile, user=request.user)
        promo = get_object_or_404(Promo, pk=promo_id, user=user.pk)
        promo.amount -= request.data['amount']
        if promo.amount < 0:
            return Response({'message': "Your promo hasn't enough amount."},
                            status=status.HTTP_400_BAD_REQUEST)
        promo.save()
        return Response({"message": "Your discount successfully"},
                        status=status.HTTP_200_OK)
