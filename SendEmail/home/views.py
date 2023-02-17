from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import random


def index(request):
    return render(request, "index.html")

def home(request):
    subject = request.POST["sub"]
    message = request.POST["msg"]
    to      = request.POST["to"]
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [to, ]
    send_mail(subject, message, email_form, recipient_list)
    return render(request, "home.html")

def genrateotp(request):
    email = request.POST["email"]
    r = random.random()
    otp = int(r*10000)
    subject = "otp"
    message = str(otp)
    to = email
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to, ]
    send_mail(subject, message, email_from, recipient_list)
    return render(request, "Varification.html", {'otp':otp})

def forgotpassword(request):
    return render(request,'forgotpassword.html')


def verifyotp(request):
    ootp = request.POST["ootp"]
    # print(ootp)
    notp = request.POST["notp"]
    # print(notp)
    if ootp==notp:
        return render(request, "changepassword.html")
    else:
        return render(request, "forgotpassword.html")










