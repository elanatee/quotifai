from flask import Flask, render_template, request
import validators
import scraper
import demo

app = Flask(__name__)

@app.route('/')
@app.route('/home')
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
                # tag=tag,
                quote=quote
            )

        else:
            return render_template(
                'error.html'
            )
