from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def send_email_view(request):
    # Logic to send email
    # For simplicity, let's assume we have already defined a function to send emails in utils.py


    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    # recipient_list = ['recipient@example.com']

    send_mail(subject, message, 'n.basha@g-japan.com', ['nisarbasha1993@gmail.com'], fail_silently=False,)

    return HttpResponse("Email sent successfully!")