from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404

import random

from app.models import SubscribedUser
from app.forms import SubscribedUserForm


class EnterNumberView(CreateView):
    template_name = "app/enter-number.html"
    model = SubscribedUser
    form_class = SubscribedUserForm
    success_url = "/enter-otp/"

    def form_valid(self, form):
        """Generates OTP and creates user instance using phone_number and otp"""
        form.instance.otp = random.randint(0000,9999)
        # insert send_otp() function here
        user = form.save()
        return redirect("enter_otp", pk=user.id)

    def form_invalid(self, form):
        phone_number = self.request.POST.get("phone_number")
        try:
            """If Number already exists go to enter OTP page without trying to create a new instance"""
            user = get_object_or_404(SubscribedUser, phone_number=phone_number)
            if user is not None:
                return redirect("enter_otp", pk=user.id)
        except:
            """if form is invalid and Number doesn't exist just show the form error"""
            pass
        return self.render_to_response(self.get_context_data(form=form))


class EnterOTPView(TemplateView):
    template_name = "app/enter-otp.html"

    def get(self, *args, **kwargs):
        """Verify if OTP inserted matches the OTP sent"""
        context = self.get_context_data(**kwargs)
        if self.request.GET.get('Resend', '') is not None:
            pass # insert send_otp() function instead of pass here
        if self.request.GET.get("Subscribe") is not None:
            subscribed_user = SubscribedUser.objects.filter(id=self.kwargs["pk"]).first()
            otp = subscribed_user.otp
            if otp == int(self.request.GET.get("OTP")):
                """If Otp entered is correct change the user status to subscribed"""
                subscribed_user.subscribed = 1
                subscribed_user.save()
                template_name2 = "app/subscribed.html"
                render_context = {
                    "phone_number": subscribed_user.phone_number,
                }
                return render(self.request, template_name2, render_context)
            else:
                messages = "WRONG OTP!!"
                return render(
                    self.request, self.template_name, {
                        "alertmessage": messages, "subscribed_user": subscribed_user
                    }
                )
        return self.render_to_response(context)
