import smtplib
import pwinput as pwd
import ssl
from email.message import EmailMessage

# Get details of email sender and receiver
email_sender = input('Email: ')
email_password = pwd.pwinput(prompt='Password: ', mask='*')
email_receiver = 'receiverEmail@gmail.com'

# Set the subject and body of the email
subject = 'Subject'
message = """
Message
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(message)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
