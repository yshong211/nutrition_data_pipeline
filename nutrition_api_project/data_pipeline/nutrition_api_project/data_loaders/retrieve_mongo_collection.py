from pymongo import MongoClient

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Setup a database retrieval function
def connect_collection(database_name: str, collection_name: str, port: int):
    # Uniform Resource Identifier for MongoDB
    uri = f'mongodb://209.182.236.218:{port}'

    # Instantiate the MongoClient
    client = MongoClient(uri)

    # Specify a database
    db = client[database_name]

    # Specify a collection
    col = db[collection_name]

    return col

@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    col_name = connect_collection('api_ninjaz', 'food', 8941)

    # Get all the documents
    docs = list(col_name.find())

    # Transform the result
    transformed_docs = [doc['result'] for doc in docs]

    # Append them via pd.concat

    return {'results' : transformed_docs}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
