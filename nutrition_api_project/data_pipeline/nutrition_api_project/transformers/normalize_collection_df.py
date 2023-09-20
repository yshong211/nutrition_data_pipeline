import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


# Transform food facts from API vendor into a PostgreSQL database
def food_fact_transform(result):
    # Transform the JSON Dictionary into a Pandas DataFrame
    df = pd.json_normalize(result)

    return df

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Use the 'results' key of the dictionary
    results = data['results']

    # Apply food transform method
    transformed_results = [food_fact_transform(result) for result in results]

    # Apply pd.concat() to the results
    df = pd.concat(transformed_results)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
