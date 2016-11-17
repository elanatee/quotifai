url = ''

from flask import Flask
from flask import render_template
from flask import request
from scraper import quote
app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html', 
        quote=quote
    )

@app.route('/next', methods=['POST'])
def next():
    if request.method == 'POST':
        url = request.form['address']
        scraped_quote = quote
        print scraped_quote
        # TODO: figure out how to call scraper and get scraped quote according to this url
        return render_template(
            'next.html', 
            greeting='hello world!'
        )