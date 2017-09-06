from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import validators
import scraper, demo

app = Flask(__name__)
app.config.from_object('config')

class ImageForm(FlaskForm):
    image_url = StringField('image_url', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()      
    if form.validate_on_submit():
        return redirect(url_for('getQuote', 
            image_url=form.image_url.data)
        )
    return render_template('index.html',
                           form=form
                           )

@app.route('/quote')
def getQuote():
    url = request.args['image_url']
    
    validURL = validators.url(url)

    if validURL:
        tag = demo.getTag(url)
        quote = scraper.scrape(tag)
        return render_template(
            'quote.html',
            tag=tag,
            quote=quote
        )

    else:
        return render_template(
            'error.html'
        )