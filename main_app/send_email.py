import smtplib
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

env = settings.ENV

def send_email(to_email,body):
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    email, password = env('email'), env('password')
    server.login(email, password)

    # Send the email
    to_email = to_email
    subject = "Password Reset"
    body = body
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail("nh.engineer@gmail.com", to_email, message)

    # Disconnect from the server
    server.quit()
