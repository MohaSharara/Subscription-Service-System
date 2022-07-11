from django.test import SimpleTestCase
from django.urls import resolve, reverse

from app.views import EnterNumberView, EnterOTPView


class TestUrls(SimpleTestCase):

    def test_enter_number_url_is_resolved(self):
        url = reverse("enter_number")
        self.assertEquals(resolve(url).func.view_class, EnterNumberView)

    def test_enter_otp_url_is_resolved(self):
        url2 = reverse("enter_otp", args=[1])
        self.assertEquals(resolve(url2).func.view_class, EnterOTPView)