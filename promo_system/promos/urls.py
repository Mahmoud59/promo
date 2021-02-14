from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from promos.api import PromoViewSet, PromoPointAPIView

router = DefaultRouter()
router.register(r'promos', PromoViewSet, basename='promos')
urlpatterns = router.urls

urlpatterns += format_suffix_patterns([
    path('promo/<int:promo_id>/', PromoPointAPIView.as_view(),
         name='promo-point'),
])
