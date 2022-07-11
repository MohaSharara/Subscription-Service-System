from django import forms

from phonenumber_field.formfields import PhoneNumberField

from app.models import SubscribedUser


class SubscribedUserForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Phone Number"
            }
        )
    )

    class Meta:
        model = SubscribedUser
        fields = "__all__"
        exclude = ["subscribed", "otp"]
