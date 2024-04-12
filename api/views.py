from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import smtplib
from email.message import EmailMessage
from validate_email import validate_email


def send_email_view(request):
    # Logic to send email
    # For simplicity, let's assume we have already defined a function to send emails in utils.py


    # subject = 'Test Email'
    # message = 'This is a test email sent from Django.'
    # # recipient_list = ['recipient@example.com']
    #
    # send_mail(subject, message, 'n.basha@g-japan.com', ['nisarbasha1993@gmail.com'], fail_silently=False,)


    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465  # SMTP SSL port
    smtp_username = 'n.basha@g-japan.com'
    smtp_password = 'nbasha2022'

    is_valid = validate_email('n.basa@g-japan.com', verify=True)
    if not is_valid:
        print("not valid")
    else:
        print("valid")

    # Create an SSL connection to the SMTP server
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)

        # Create and send the email message
        msg = EmailMessage()
        msg.set_content('This is a test email sent using SMTP_SSL')
        msg['Subject'] = 'Test Email'
        msg['From'] = smtp_username
        msg['To'] = 'nisarbasha1993@gmail.com'

        server.send_message(msg)

        # Close the connection
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error sending email: {e}')

    return HttpResponse("Email sent successfully!")