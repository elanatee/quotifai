from flask import Flask
from flask import render_template
from demo import tag
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', tag=tag)