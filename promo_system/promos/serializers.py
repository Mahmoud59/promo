from rest_framework import serializers

from promos.models import Promo


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'
