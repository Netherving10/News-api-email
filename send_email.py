import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("MAIL_LOGIN")
    password = os.getenv("MAIL_PASSWORD")
    reciever = os.getenv("MAIL_LOGIN")
    # create ssl connection
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
