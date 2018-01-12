import urllib.request
import json
from .model import Meals

def get_sources(meals):
    """Function to retrieve meals  list from the api"""

    get_url = 'http://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood'

    #  get_url = 'http://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}'

    # meal_name = request.args.get('meal_name')

    with urllib.request.urlopen(get_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)

        sources_results = None

        if get_response['meals']:
            sources_results_list = get_response['meals']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(meals_list):
    """Function that process the results list and transforms them into a list of objects
    Args: meals_list: A list of dictionaries that contains news sources details

    Returns:
    sources_results: a list of news sources objects"""

    sources_results = []
    for source_item in meals_list:
        idMeal = source_item.get('idMeal')
        strMeal = source_item.get('strMeal')
        strCategory = source_item.get('strCategory')
        strArea = source_item.get('strArea')
        strInstructions = source_item.get('strInstructions')
        strMealThumb = source_item.get('strMealThumb')
        strTags = source_item.get('strTags')
        strMeasure1 = source_item.get('strMeasure1')
        strIngridients1 = source_item.get('strIngridients1')
        strYoutube = source_item.get('strYoutube')

        source_object = Meals(idMeal, strMeal, strCategory, strArea, strInstructions, strMealThumb, strTags, strMeasure1, strIngridients1, strYoutube)
        sources_results.append(source_object)

    return sources_results
