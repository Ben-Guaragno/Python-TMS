#!/home/ben/python/bin/python

import smtplib, ssl
from email.message import EmailMessage
import secret_loader

def send_email(subject,body):
    secrets=secret_loader.read()
    PORT = secrets["PORT"]
    SMTP_SERVER = secrets["SMTP_SERVER"]
    SENDER_EMAIL = secrets["SENDER_EMAIL"]
    SENDER_EMAIL_PRETTY = secrets["SENDER_EMAIL_PRETTY"]
    RECEIVER_EMAIL = secrets["RECEIVER_EMAIL"]
    PASSWORD = secrets["PASSWORD"] #App password

    msg = EmailMessage()
    msg.set_content(body+"\n\n\nBest,\nZero")
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL_PRETTY
    msg['To'] = RECEIVER_EMAIL

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.send_message(msg, from_addr=SENDER_EMAIL_PRETTY, to_addrs=RECEIVER_EMAIL)

