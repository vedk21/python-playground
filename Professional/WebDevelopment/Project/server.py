from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('./index.html')

# generic html routing
@app.route('/<string:html_page>')
def generic_page(html_page='index.html'):
  return render_template(html_page)

# handle contact form request
@app.route('/submit_contact_form', methods = ['POST', 'GET'])
def submit_contact_form():
  if request.method == 'POST':
    form_data = request.form.to_dict()
    save_contact_data_to_csv(form_data)
    return 'Form submitted'
  else:
    return 'Error: Please try again later.'

def save_contact_data_to_file(contact_data):
  with open('./database/db.txt', 'a') as db:
    contact_name = contact_data['contact_name']
    contact_email = contact_data['contact_email']
    subject = contact_data['subject']
    message = contact_data['message']

    db.write(f'\n{contact_name}, {contact_email}, {subject}, {message}')

def save_contact_data_to_csv(contact_data):
  with open('./database/db.csv', newline = '', mode = 'a') as db:
    contact_name = contact_data['contact_name']
    contact_email = contact_data['contact_email']
    subject = contact_data['subject']
    message = contact_data['message']

    csv_writer = csv.writer(db, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    csv_writer.writerow([contact_name, contact_email, subject, message])
