url = ''

from flask import Flask
from flask import render_template
from flask import request
import scraper
import demo
app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html'
    )

@app.route('/next', methods=['POST'])
def next():
    if request.method == 'POST':
        url = request.form['address']
        tag = demo.getTag(url)
        quote = scraper.scrape(tag)
        return render_template(
            'next.html', 
            greeting=quote
        )