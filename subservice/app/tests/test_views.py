from django.test import TestCase, Client
from django.urls import reverse

from app.models import SubscribedUser


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.enter_number_url = reverse('enter_number')
        self.enter_otp_url = reverse('enter_otp', args=[1])
        self.subscribeduser1 = SubscribedUser.objects.create(
            id=1,
            phone_number="+96170813991",
            otp="9999"
        )

    def test_enter_number_url_GET(self):
        # Test the get method on enter number page
        response = self.client.get(self.enter_number_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/enter-number.html")

    def test_enter_otp_url_GET(self):
        # Test the get method on enter otp page
        response = self.client.get(self.enter_otp_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/enter-otp.html")

    def test_enter_number_url_POST(self):
        # Test the post method on enter number page
        response = self.client.post(self.enter_number_url, {
            "phone_number": "+96170813991",
        })
        self.assertEquals(response.status_code, 302)

    def test_enter_number_url_POST_no_data_or_wrong_data(self):
        # Testing no data entry or wrong data entry cases work
        response = self.client.get(self.enter_number_url)
        response2 = self.client.post(self.enter_number_url, {
            "phone_number": "55",
        })

        self.assertNotEqual(response.status_code, 302)
        self.assertNotEqual(response2.status_code, 302)

    def test_enter_otp_url_Success(self):
        """
        Check if OTP 9999 for user of ID 1
        that we created subscribes succesfully
        """
        response = self.client.get('/enter-otp/1/?OTP=9999&Subscribe=/')
        subscribeduser = SubscribedUser.objects.get(id=1)
        self.assertEquals(subscribeduser.subscribed, 1)
        self.assertTemplateUsed(response, "app/subscribed.html")
