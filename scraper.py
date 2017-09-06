from bs4 import BeautifulSoup
import requests

def scrape(tag):
    tag = tag.replace(' ', '+') 
    result = requests.get('http://www.goodreads.com/quotes/tag/' + tag)
    c = result.content

    soup = BeautifulSoup(c, 'html.parser')

    samples = soup.find_all("div", "quoteText") # gets list of all divs with class "quoteText"
    
    if not samples: # no quotes found, empty list
        return None 

    text = samples[0].get_text() # extract text from BeautifulSoup result

    quote = ''
    for char in text:
        if char != '/':
            quote += char
        else:
            break # stop scraping at javascript in div

    return quote