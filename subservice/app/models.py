from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class SubscribedUser(models.Model):
    phone_number = PhoneNumberField(unique=True)
    otp = models.IntegerField(default=9999)
    subscribed = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.phone_number} ID={self.id}"
