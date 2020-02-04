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

    
    news = get_sources('sources')
    return render_template('index.html', title=title, sources= news)
