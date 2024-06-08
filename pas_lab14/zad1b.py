import smtplib
import ssl


def send_email():
    sender_email = input("Enter your email address: ")
    receiver_email = input("Enter recipient's email address: ")
    subject = input("Enter the subject: ")
    message = input("Enter the message: ")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('interia.pl', 465, context=context) as server:
        server.ehlo()

        server.login(sender_email, 'your_password')

        email_content = f"Subject: {subject}\n\n{message}"

        server.sendmail(sender_email, receiver_email, email_content)


send_email()
