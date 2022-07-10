from django.urls import path

from app.views import EnterNumberView, EnterOTPView

urlpatterns = [
    path("", EnterNumberView.as_view(), name="enter_number"),
    path("enter-otp/<pk>/", EnterOTPView.as_view(), name="enter_otp"),
]
