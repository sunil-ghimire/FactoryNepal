import smtplib
from FactoryNepal.settings import env


def send_email(to_email):
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    email, password = env('email'), env('password')
    server.login(email, password)

    # Send the email
    to_email = to_email
    subject = "Password Reset"
    body = "test body for email reset"
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail("nh.engineer@gmail.com", to_email, message)

    # Disconnect from the server
    server.quit()
