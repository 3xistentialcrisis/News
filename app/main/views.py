from flask import render_template,request, redirect, url_for
from . import main
from ..models import Sources
from ..requests import get_news, get_sources

@main.route('/')
def index():
    '''
    This function returns the application index page
    '''

    news_sources = get_sources()
    return render_template('index.html',  sources= news_sources)

