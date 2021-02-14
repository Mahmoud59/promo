from unittest.mock import patch, MagicMock

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from promos.models import Promo
from tests.constants import PROMO_TYPE_1, PROMO_START_TIME_1, \
    PROMO_AMOUNT_1, PROMO_END_TIME_1, PROMO_DESCRIPTION_1, PROMO_CODE_1, \
    PROMO_TYPE_2, PROMO_CODE_2, PROMO_START_TIME_2, PROMO_END_TIME_2, \
    PROMO_DESCRIPTION_2, PROMO_AMOUNT_2, USER_UUID_1, \
    USER_MOBILE_NUMBER_1, USER_USERNAME_1, USER_ADDRESS_1, USER_EMAIL_1
from users.models import UserProfile


@pytest.mark.django_db
class TestPromoEndpoints:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.user = User.objects.create(email=USER_EMAIL_1)
        self.user = UserProfile.objects.create(
            uuid=USER_UUID_1, username=USER_USERNAME_1,
            address=USER_ADDRESS_1, mobile_number=USER_MOBILE_NUMBER_1,
            user=self.user
        )
        self.promo = Promo.objects.create(
            type=PROMO_TYPE_1, code=PROMO_CODE_1,
            start_time=PROMO_START_TIME_1, end_time=PROMO_END_TIME_1,
            amount=PROMO_AMOUNT_1, description=PROMO_DESCRIPTION_1,
            status=Promo.PromoStatus.ACTIVE, user=self.user
        )
        self.url_list = reverse('promos-list')
        self.url_detail = reverse('promos-detail',
                                  kwargs={'pk': self.promo.id})

    @patch('promos.permissions.PromoPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_list_promos_success(self, mock_authenticate, mock_permission,
                                 drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_promos_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('promos.permissions.PromoPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_create_promo_success(self, mock_authenticate, mock_permission,
                                  drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        body = {
            "type": PROMO_TYPE_2,
            "code": PROMO_CODE_2,
            "start_time": PROMO_START_TIME_2,
            "end_time": PROMO_END_TIME_2,
            "amount": PROMO_AMOUNT_2,
            "description": PROMO_DESCRIPTION_2,
            "user": self.user.pk
        }
        response = drf_client.post(self.url_list, data=body, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_promo_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('promos.permissions.PromoPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_retrieve_promo_success(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_retrieve_promo_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('promos.permissions.PromoPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_update_promo_sucess(self, mock_authenticate, mock_permission,
                                 drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        body = {
            "type": PROMO_TYPE_2,
            "code": PROMO_CODE_2,
            "start_time": PROMO_START_TIME_2,
            "end_time": PROMO_END_TIME_2,
            "amount": PROMO_AMOUNT_2,
            "description": PROMO_DESCRIPTION_2,
        }
        response = drf_client.patch(self.url_detail, data=body, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_promo_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('promos.permissions.PromoPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_delete_promo_sucess(self, mock_authenticate, mock_permission,
                                 drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        response = drf_client.delete(self.url_detail)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_promo_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestPromoPointEndpoint:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.user = User.objects.create(email=USER_EMAIL_1)
        self.user_profile = UserProfile.objects.create(
            uuid=USER_UUID_1, username=USER_USERNAME_1,
            address=USER_ADDRESS_1, mobile_number=USER_MOBILE_NUMBER_1,
            user=self.user
        )
        self.promo = Promo.objects.create(
            type=PROMO_TYPE_1, code=PROMO_CODE_1,
            start_time=PROMO_START_TIME_1, end_time=PROMO_END_TIME_1,
            amount=PROMO_AMOUNT_1, description=PROMO_DESCRIPTION_1,
            status=Promo.PromoStatus.ACTIVE, user=self.user_profile
        )
        self.url_detail = reverse('promo-point',
                                  kwargs={'promo_id': self.promo.id})

    @patch('users.permissions.UserPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_use_promo_success(self, mock_authenticate, mock_permission,
                               drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        body = {
            "amount": PROMO_AMOUNT_2
        }
        response = drf_client.post(self.url_detail, data=body, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_use_promo_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
