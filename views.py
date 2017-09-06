from flask import Flask, render_template, request, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from secret import secret_key
import validators
import scraper, demo

app = Flask(__name__)
app.config.from_object('config')

class ImageForm(FlaskForm):
    url = StringField('url', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()      
    if form.validate_on_submit():
        return redirect(url_for('getQuote', 
            url=form.url.data)
        )
    return render_template('index.html',
                           form=form
                           )

@app.route('/quote')
def getQuote():
    if not request.args:
        return render_template('error.html')

    url = request.args['url']
    
    validURL = validators.url(url)

    if validURL:
        quote = None
        if 'tag_index' in request.args: # if a tag # is specified in request, use it
            tag_index = int(request.args['tag_index']) # unicode -> int
            
        else: # otherwise start w/ the first tag
            tag_index = 0 
            tags, tag = demo.getTag(url, tag_index)
            session['tags'] = tags

        if 'tags' in session: # if list of tags in session 
            tags = session['tags']

        while quote == None: # find tags that give quote results
            if tag_index == 20: # reset to first tag when at end of list
                tag_index = 0
            tag = tags[tag_index]
            quote = scraper.scrape(tag)
            tag_index += 1 

        return render_template(
            'quote.html',
            url=url,
            tag=tag,
            quote=quote,
            tag_index=tag_index
        )

    else:
        return render_template(
            'error.html'
        )

app.secret_key = secret_key

# TO DO: 
# get next quote for same tag