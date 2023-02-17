from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("home", views.home),
    path("genrateotp", views.genrateotp),
    path("verifyotp", views.verifyotp),
    path("forgotpassword", views.forgotpassword),


]