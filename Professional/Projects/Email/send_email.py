# Send email

import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Vedant Kakade Python Test'
email['to'] = 'vedantkakade.cp@gmail.com'
email['subject'] = 'Hi, Welcome to Python Jumanji'

email.set_content('Here is your free test pass for Python Jumnaji.')

# setup smtp server
with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('', '') # enter valid emailId, password
  smtp.send_message(email)
  print('Email sent successfully')
