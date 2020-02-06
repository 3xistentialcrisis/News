from flask import render_template, request, redirect, url_for
from . import main
from ..models import Sources
from ..requests import get_news, get_sources


@main.route('/')
def index():
    '''
    This function returns the application index page
    '''

    news_sources = get_sources()
    return render_template('index.html', sources=news_sources)


@main.route("/news/<source_id>")
def news(source_id):
    """
    This function returns the articles based on their sources
    """

    articles_sources = get_news(source_id)
    return render_template('index.html', articles_sources=articles_sources, name=source_id)
