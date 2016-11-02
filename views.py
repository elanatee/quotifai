from flask import Flask
from flask import render_template
from scraper import quote
app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html', 
        quote=quote
        )