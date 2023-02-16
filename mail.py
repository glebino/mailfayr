mport smtplib, ssl
from fileinput import filename

from envelope import Envelope
from pathlib import Path

def sendmail(filename):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "sender@domain.com"
    receiver_email = ["smth@yandex.com", "smth.else@domain.com"]
    password = "ETk57wK91"

    send_file = filename

    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)

    #email send zone

        Envelope()\
            .from_(sender_email)\
            .subject("test")\
            .to(receiver_email)\
            .message("")\
            .attach(Path(filename))\
            .smtp(smtp_server, port, sender_email, password)\
            .send()

        server.quit()

file = '/app/file.txt'
sendmail(file)