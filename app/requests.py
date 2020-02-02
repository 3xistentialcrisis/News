import urllib.request
import json
from .models import News,Sources

#Get the API key
api_key = None

#Get the News base url
base_url = None

#Function that takes in the application instance
def configure_request(app)
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']