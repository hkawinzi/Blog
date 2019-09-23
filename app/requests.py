import urllib.request,json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']

def get_quotes():
    '''
    This function fetches the quotes using the quotes api
    '''
    with urllib.request.urlopen(base_url) as url:
        quotes_data = url.read()
        random_quote = json.loads(quotes_data)
        print(random_quote)
        quotes_result = []