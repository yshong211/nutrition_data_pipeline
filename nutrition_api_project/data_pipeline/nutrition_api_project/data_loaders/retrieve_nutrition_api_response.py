import requests
from datetime import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# helper Functions

# API Selection function
def nutrition_api_select(api_vendor: str, food_name: str):
    if api_vendor == 'dietagram':
        url = "https://dietagram.p.rapidapi.com/apiFood.php"
        
        # Query parameters for the API
        querystring = {"name":food_name,"lang":"en"}

        host = "dietagram.p.rapidapi.com"
    
    elif api_vendor == 'api-ninjas':
        url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"
        
        # Query parameters for the API
        querystring = {"query": food_name}

        host = "nutrition-by-api-ninjas.p.rapidapi.com"
    
    return url, querystring, host

# Create a function to pass in any English food name
def retrieve_food_facts_json(food_name: str, api_vendor: str):
    
    # Retrieve the URL, Querystring, and API Host from RapidAPI
    api_inputs = nutrition_api_select(api_vendor, food_name)

    # Assign the values in the tuple to separate variables for url, query, and host
    url, querystring, host = api_inputs
    
    # # Actual endpoint for Food API
    # url = "https://dietagram.p.rapidapi.com/apiFood.php"

    # # Query parameters for the API
    # querystring = {"name":food_name,"lang":"en"}

    # Headers for food API endpoint from Dietagram
    headers = {
        "X-RapidAPI-Key": "90d6f20e25msh26f3b3c0cc23025p1fa1dajsn46ee4c3bd0d5",
        "X-RapidAPI-Host": host
    }

    # GET request response
    response = requests.get(url, headers=headers, params=querystring)

    # JSON result
    result = response.json()

    return result


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here

    result_list = []

    # Specify list of food names
    food_names = ['wings', 'clam chowder']

    # Iterate through the helper function
    for food_name in food_names:
        # JSON response for the particular food
        food_resp = retrieve_food_facts_json(food_name, 'api-ninjas')

        # Convert into a dictionary
        json_repr = {'result' : food_resp, 'updatedAt': str(datetime.now())}

        # Add the response to the result list
        result_list.append(json_repr)

    return result_list


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

