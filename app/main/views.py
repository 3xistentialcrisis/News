from flask import render_template,request, redirect, url_for
from . import main
from ..models import Sources
from ..requests import get_news, get_sources

@main.route('/')
def index():
    '''
    This function returns the application index page
    '''

    title = 'Home || Welcome to your Daily News Aggregator'

    news_sources  = get_sources('source')
    return render_template('index.html', title=title, source= news_sources)

