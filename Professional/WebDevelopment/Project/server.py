from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./home.html')

@app.route('/blog/<username>/<int:blog_id>')
def blog(username, blog_id):
    return render_template('./blog.html', username = username, blog_id = blog_id)
