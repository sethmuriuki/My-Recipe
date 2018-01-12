from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_sources

# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    meal_sources = get_sources('meals')

    return render_template('index.html', meal_sources = meal_sources)

@main.route('/categories')
def category():
    '''
    display recipes category
    '''
    meal_sources = get_sources('meals')

    return render_template('category.html', meal_sources = meal_sources)
