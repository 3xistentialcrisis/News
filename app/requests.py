import urllib.request
import json
from .models import News,Sources
from newsapi import NewsApiClient

#Get the API key
api_key = None

#Get the News base url
base_url = None

#Function that takes in the application instance
def configure_request(app)
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

#News Request 
def get_news(id):
    '''
    This function retrieves the news articles from their source
    '''
    get_news_link = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    # get_news_link = 'https://newsapi.org/v2/top-headlines?sources?apiKey=3540aa7416f144918cf919d37f574a5c'.format(id,api_key)

    with urllib.request.urlopen(get_news_link) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['news']:
            news_results = process_news(get_news_response['news'])

    return news_results

#Process News 
def process_news(news_array):
    '''
    This Function  processes the json news results and transforms them to a list of objects
    '''
    
    #news object
    news_results = []

    for news_item in news_array:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')

        compiled_news = News(author, title, description, urlToImage, url, publishedAt)
        news_results.append(compiled_news)

    return news_results


#Sources Request
def get_sources(source):
    '''
    This Function gets news sources from the News API
    '''

    get_sources_link = 'https://newsapi.org/v2/sources?apiKey=3540aa7416f144918cf919d37f574a5c'.format(source,api_key)

    with urllib.request.urlopen(get_sources_link) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results = process_results(get_sources_response['sources'])
    
    return sources_results

#Process Sources
def process_results(sources_array):
    '''
    This Function  processes and transforms sources into a objects list
    '''
    #sources object
    sources_results = []
    for source_item in sources_array:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        country = source_item.get('country')
        url = source_item.get('url')
        

        source_object = Sources(id, name, description, category, country, url)
        sources_results.append(source_object)

    return sources_results