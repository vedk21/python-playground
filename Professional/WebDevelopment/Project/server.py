from flask import Flask, render_template, request, redirect
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
    print(form_data)
    return 'Form submitted'
  else:
    return 'Error: Please try again later.'
