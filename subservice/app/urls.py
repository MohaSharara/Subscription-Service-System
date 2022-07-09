from django.urls import path

from app.views import EnterNumberView, EnterOTPView, SubscribedView

urlpatterns = [
    path("", EnterNumberView.as_view(), name="enter_number"),
    path("enter-otp/<pk>/", EnterOTPView.as_view(), name="enter_otp"),
    path("subscribed", SubscribedView.as_view(), name="subscribed"),
    path("resend-otp", SubscribedView.as_view(), name="resend_otp"),
]
