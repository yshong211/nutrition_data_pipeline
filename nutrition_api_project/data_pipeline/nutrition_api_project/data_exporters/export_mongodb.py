from pymongo import MongoClient

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


# Helper Functions
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

# Setup a function which would push a dictionary as a new object within the collection
def push_object(col, obj: dict):
    # Use the insert_one method
    col.insert_one(obj)

    
@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: List of JSON responses from the previous step in the pipeline.
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    
    col = connect_collection('api_ninjaz', 'food', 8941)

    for resp in data:
        # Push to MongoDB
        push_object(col, resp)


