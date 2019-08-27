#!/usr/bin/python

import smtplib
from getpass import getpass
from email.mime.text import MIMEText

your_email = "your.email@example.com"
your_password = getpass()

# This will help us with the email format
message = MIMEText('Ceci est un test !')
message['Subject'] = 'Objet du message'

message['From'] = 'your.email@example.com'
message['To'] = 'your.email@example.com'  # You can send an email at yourself to test


try:
    # We can find these informations here : https://support.office.com/en-us/article/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040?omkt=en-001&ui=en-US&rs=en-001&ad=US
    # You can try to use it with gmail for example, you will have to your gmail account for it
    smtpObj = smtplib.SMTP('SMTP.office365.com', 587)
    smtpObj.starttls()  # Port 587 mean that we have to use encrypted communication with TLS
    smtpObj.login(your_email, your_password)
    smtpObj.send_message(message)
    print("Successfully sent email")
    input()
except Exception:
    print("Error: unable to send email")
    input()
