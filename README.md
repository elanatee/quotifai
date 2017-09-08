# quotifai :camera:

> a web app that displays a quote related to a submitted image

<img src='static/quotifai.png'>

## technologies used:
- [Clarifai API](https://clarifai.com/developer/)
- [Flask](http://flask.pocoo.org/docs/0.11/quickstart/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## how it works
- `demo.py` uses Clarifai's image recognition API to analyze an image and generate a list of tags based on the image content
- `scraper.py` retrieves quotes from Goodreads.com based on the image tags.

## setup + run
to get this code up and running on your own machine,

0. make sure you have [Python](https://www.python.org/downloads/) and the [pip package installer](https://pip.pypa.io/en/stable/installing/)
1. clone this repository (or download it to your desktop)
2. in terminal, navigate to the project directory
    ```
    $ cd /path/to/quotifai
    ```
3. install the required Python packages 
    ```
    $ pip install -r requirements.txt
    ```
4. get a Clarifai API key from [developer.clarifai.com](https://developer.clarifai.com) and follow [these instructions](https://github.com/Clarifai/clarifai-python) (under `Setup`) to configure it on your machine
5. tell Flask which application to work with by setting the FLASK_APP environment variable:
    - on MacOS/Linux: `$ export FLASK_APP=app.py`
    - on Windows: `$ set FLASK_APP=app.py`
6. now you can run the app using `flask run`, and navigate to http://127.0.0.1:5000/ to see it live! your terminal should look like this:
    ```
    $ flask run
     * Serving Flask app "app"
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```
## resources & further reading
- [Clarifai API Python Client](https://github.com/Clarifai/clarifai-python)
- [The Flask Mega-Tutorial, Part III: Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms) by Miguel Grinberg
- [Flask Quickstart](http://flask.pocoo.org/docs/0.12/quickstart/#quickstart)

## thanks!
feedback and pull requests are warmly welcomed and encouraged! 

tweet me [@elanatee](https://twitter.com/elanatee) if you have any questions!