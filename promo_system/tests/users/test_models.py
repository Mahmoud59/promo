import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from tests.constants import ADMIN_UUID_1, ADMIN_USERNAME_1, ADMIN_ADDRESS_1, \
    ADMIN_EMAIL_1, ADMIN_USERNAME_2, ADMIN_ADDRESS_2, \
    ADMIN_EMAIL_2, USER_EMAIL_1, USER_UUID_1, USER_ADDRESS_1, USER_USERNAME_1,\
    USER_MOBILE_NUMBER_1, USER_ADDRESS_2, USER_USERNAME_2, \
    ADMIN_UUID_2, USER_EMAIL_2, USER_UUID_2
from users.models import Admin, UserProfile


@pytest.mark.django_db
class TestAdminModel:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.user = User.objects.create(email=ADMIN_EMAIL_1)
        self.admin = Admin.objects.create(
            uuid=ADMIN_UUID_1, username=ADMIN_USERNAME_1,
            address=ADMIN_ADDRESS_1, user=self.user
        )

    def test_list_admins_objects_success(self):
        assert Admin.objects.all().count() == 1

    def test_create_admin_objects_success(self):
        self.user_2 = User.objects.create(email=ADMIN_EMAIL_2,
                                          username=ADMIN_USERNAME_2)
        Admin.objects.create(uuid=ADMIN_UUID_2, username=ADMIN_USERNAME_2,
                             address=ADMIN_ADDRESS_2, user=self.user_2)
        assert Admin.objects.all().count() == 2

    def test_retrieve_admin_object_success(self):
        assert len(Admin.objects.filter(uuid=self.admin.uuid)) == 1

    def test_retrieve_admin_object_fail_with_not_exist_id(self):
        with pytest.raises(ObjectDoesNotExist):
            Admin.objects.get(uuid=5)


@pytest.mark.django_db
class TestUserModel:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.user = User.objects.create(email=USER_EMAIL_1)
        self.users_profile = UserProfile.objects.create(
            uuid=USER_UUID_1, username=USER_USERNAME_1,
            address=USER_ADDRESS_1, mobile_number=USER_MOBILE_NUMBER_1,
            user=self.user
        )

    def test_list_admins_objects_success(self):
        assert UserProfile.objects.all().count() == 1

    def test_create_user_objects_success(self):
        self.user_2 = User.objects.create(
            email=USER_EMAIL_2, username=USER_USERNAME_2)
        UserProfile.objects.create(
            uuid=USER_UUID_2, username=USER_USERNAME_2,
            address=USER_ADDRESS_2, user=self.user_2)
        assert UserProfile.objects.all().count() == 2

    def test_retrieve_user_object_success(self):
        assert len(UserProfile.objects.filter(
            uuid=self.users_profile.uuid)) == 1

    def test_retrieve_user_object_fail_with_not_exist_id(self):
        with pytest.raises(ObjectDoesNotExist):
            UserProfile.objects.get(uuid=5)
