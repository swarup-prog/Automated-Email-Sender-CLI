import smtplib
import pwinput as pwd
import ssl
from email.message import EmailMessage
import pandas as pd
import numpy as np

# Get details of email sender and receiver
# email_sender = input('Email: ')
# email_password = pwd.pwinput(prompt='Password: ', mask='*')

# Extracting emails from csv 
csv_data = pd.read_csv('test-data.csv')
email_receivers = list(csv_data['Email'].values)
print(email_receivers)

# Set the subject and body of the email
# subject = 'Subject'
# message = """
# Message
# """

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(message)

# # Add SSL (layer of security)
# context = ssl.create_default_context()

# # Log in and send the email
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())
