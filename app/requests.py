import requests

def getQuotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quotes = response.json()
        print(quotes)
        return quotes