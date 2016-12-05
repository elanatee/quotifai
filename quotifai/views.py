from flask import Flask
from flask import render_template
from flask import request
from quotifai import app
import validators
import scraper
import demo

@app.route('/')
def home():
    return render_template(
        'index.html'
    )

@app.route('/quote', methods=['POST'])
def getQuote():
    if request.method == 'POST':
        url = request.form['address']
        validURL = validators.url(url)

        if validURL:
            tag = demo.getTag(url)
            quote = scraper.scrape(tag)
            return render_template(
                'quote.html', 
                quote=quote
            )

        return render_template(
            'error.html'
        )