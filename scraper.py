from bs4 import BeautifulSoup
import requests

def scrape(tag):

    result = requests.get('http://www.goodreads.com/quotes/tag/' + tag)
    c = result.content

    soup = BeautifulSoup(c, 'html.parser')

    samples = soup.find_all("div", "quoteText")

    text = samples[0].get_text()

    # super hacky way of parsing result lol!
    quote = ' '
    for char in text:
        if char != '/':
            quote += char
        else:
            break

    return quote