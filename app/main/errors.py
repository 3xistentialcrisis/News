from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_0_four(error):
    '''
    This Function renders the 404 error page
    '''
    return render_template('404-error.html'),404