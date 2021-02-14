import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from promos.models import Promo
from tests.constants import PROMO_TYPE_1, PROMO_CODE_1, \
    PROMO_END_TIME_1, PROMO_DESCRIPTION_1, \
    PROMO_AMOUNT_1, PROMO_START_TIME_1, PROMO_CODE_2, PROMO_TYPE_2, \
    PROMO_START_TIME_2, PROMO_END_TIME_2, PROMO_DESCRIPTION_2, PROMO_AMOUNT_2,\
    USER_ADDRESS_1, USER_UUID_1, USER_USERNAME_1, USER_MOBILE_NUMBER_1, \
    USER_EMAIL_1
from users.models import UserProfile


@pytest.mark.django_db
class TestPromoModel:
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

    def test_list_promos_objects_success(self):
        assert Promo.objects.all().count() == 1

    def test_create_promo_objects_success(self):
        Promo.objects.create(
            type=PROMO_TYPE_2, code=PROMO_CODE_2,
            start_time=PROMO_START_TIME_2, end_time=PROMO_END_TIME_2,
            amount=PROMO_AMOUNT_2, description=PROMO_DESCRIPTION_2,
            status=Promo.PromoStatus.ACTIVE, user=self.user
        )
        assert Promo.objects.all().count() == 2

    def test_retrieve_promo_object_success(self):
        assert len(Promo.objects.filter(pk=self.promo.id)) == 1

    def test_retrieve_promo_object_fail_with_not_exist_id(self):
        with pytest.raises(ObjectDoesNotExist):
            Promo.objects.get(pk=5)
