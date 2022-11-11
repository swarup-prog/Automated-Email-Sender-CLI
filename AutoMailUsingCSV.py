import smtplib
import pwinput as pwd
import ssl
from email.message import EmailMessage
import pandas as pd

# Get details of email sender and receiver
email_sender = input('Email: ')
email_password = pwd.pwinput(prompt='Password: ', mask='*')

# Extracting email receivers  from csv 
csv_data = pd.read_csv('YourCSVFileName.csv')

# Use the name of the column that has emails in your CSV file
email_receivers = list(csv_data['Email'].values)

# Set the subject and body of the email
subject = 'Subject of your mail'
message = """
Your Message
"""

for email_receiver in email_receivers:
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(message)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("Email sent to " + email_receiver)
    except Exception as e:
        print("Email couldnot be sent to " + email_receiver)
        print(e)
