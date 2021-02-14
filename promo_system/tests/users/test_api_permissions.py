from unittest.mock import patch, MagicMock

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from tests.constants import ADMIN_UUID_1, ADMIN_USERNAME_1, ADMIN_ADDRESS_1, \
    ADMIN_EMAIL_1, ADMIN_USERNAME_2, ADMIN_PASSWORD_1, ADMIN_ADDRESS_2, \
    USER_EMAIL_1, USER_UUID_1, USER_ADDRESS_1, USER_USERNAME_1, \
    USER_MOBILE_NUMBER_1, USER_ADDRESS_2, USER_USERNAME_2, USER_PASSWORD_1, \
    USER_MOBILE_NUMBER_2
from users.models import Admin, UserProfile


@pytest.mark.django_db
class TestAdminPermissionEndpoints:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.user = User.objects.create(email=ADMIN_EMAIL_1)
        self.admin = Admin.objects.create(
            uuid=ADMIN_UUID_1, username=ADMIN_USERNAME_1,
            address=ADMIN_ADDRESS_1, user=self.user
        )
        self.url_list = reverse('admins-list')
        self.url_detail = reverse('admins-detail',
                                  kwargs={'pk': self.admin.uuid})

    @patch('users.permissions.AdminPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_list_admins_without_permission(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_admins_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('users.permissions.AdminPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_create_admin_without_permission(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        body = {
            "username": ADMIN_USERNAME_2,
            "password": ADMIN_PASSWORD_1,
            "address": ADMIN_ADDRESS_2,
        }
        response = drf_client.post(self.url_list, data=body, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_admin_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('users.permissions.AdminPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_retrieve_admin_without_permission(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_retrieve_admin_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('users.permissions.AdminPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_update_admin_without_permission(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        body = {
            "username": ADMIN_USERNAME_2,
            "address": ADMIN_ADDRESS_2
        }
        response = drf_client.patch(self.url_detail, data=body, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_admin_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('users.permissions.AdminPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_delete_admin_without_permission(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        response = drf_client.delete(self.url_detail)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_admin_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestUserEndpoints:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.user = User.objects.create(email=USER_EMAIL_1)
        self.users_profile = UserProfile.objects.create(
            uuid=USER_UUID_1, username=USER_USERNAME_1,
            address=USER_ADDRESS_1, mobile_number=USER_MOBILE_NUMBER_1,
            user=self.user
        )
        self.url_list = reverse('users-list')
        self.url_detail = reverse('users-detail',
                                  kwargs={'pk': self.users_profile.uuid})

    @patch('users.permissions.UserPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_list_users_without_permission(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list__user_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('users.permissions.UserPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_create_user_without_permission(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        body = {
            "username": USER_USERNAME_2,
            "password": USER_PASSWORD_1,
            "address": USER_ADDRESS_2,
            "mobile_number": USER_MOBILE_NUMBER_2
        }
        response = drf_client.post(self.url_list, data=body, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create__user_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('users.permissions.UserPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_update_user_without_permission(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        body = {
            "username": USER_USERNAME_2,
            "address": USER_ADDRESS_2,
            "mobile_number": USER_MOBILE_NUMBER_2
        }
        response = drf_client.patch(self.url_detail, data=body, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_user_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('users.permissions.UserPermission.has_permission')
    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_delete_user_without_permission(
            self, mock_authenticate, mock_permission, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        mock_permission.return_value = False
        response = drf_client.delete(self.url_detail)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_user_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
