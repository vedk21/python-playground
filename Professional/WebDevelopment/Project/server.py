from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

# generic html routing
@app.route('/<string:html_page>')
def generic_page(html_page='index.html'):
    return render_template(html_page)
