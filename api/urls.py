from django.urls import path
from .views import *

urlpatterns = [

    path('send_email_view', send_email_view),
    ]