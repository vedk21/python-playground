# Send email in HTML format

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()
html = Template(Path('email_template.html').read_text())

email['from'] = 'Vedant Kakade Python Test'
email['to'] = 'vedantkakade.cp@gmail.com'
email['subject'] = 'Hi, Welcome to Python Jumanji'

email.set_content(html.substitute(xx = '300'), 'html')

# setup smtp server
with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('', '') # enter valid emailId, password
  smtp.send_message(email)
  print('HTML content email sent successfully')

