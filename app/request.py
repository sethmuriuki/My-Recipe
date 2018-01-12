import urllib.request
import json
from .model import Meals, Category,Search

def get_sources(meals):
    """
    Function to retrieve meals  list from the api
    """

    get_latest_url = 'http://www.themealdb.com/api/json/v1/1/latest.php'
    get_category_url = 'http://www.themealdb.com/api/json/v1/1/list.php?c=list'
    get_search_url = 'http://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata'

    
# latest results
    with urllib.request.urlopen(get_latest_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)

        latest_results = None

        if get_response['meals']:
            sources_results_list = get_response['meals']
            latest_results = process_results(sources_results_list)

    return latest_results

# category results
    with urllib.request.urlopen(get_category_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)

        category_results = None

        if get_response['meals']:
            sources_results_list = get_response['meals']
            category_results = process_results(sources_results_list)

    return category_results

# search results
    with urllib.request.urlopen(get_search_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)

        search_results = None

        if get_response['meals']:
            sources_results_list = get_response['meals']
            search_results = process_results(sources_results_list)

    return search_results

def process_results(meals_list):
    """Function that process the results list and transforms them into a list of objects
    Args: meals_list: A list of dictionaries that contains meals details

    Returns:
    results: a list of meal objects"""
    
# latest
    latest_results = []
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
        latest_results.append(source_object)

    return latest_results

# category
    category_results = []
    for source_item in meals_list:
        strCategory = source_item.get('strCategory')
        source_object = Category(strCategory)
        category_results.append(source_object)

    return category_results

# search
    search_results = []
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

        source_object = Search(idMeal, strMeal, strCategory, strArea, strInstructions, strMealThumb, strTags, strMeasure1, strIngridients1)
        search_results.append(source_object)

    return latest_results