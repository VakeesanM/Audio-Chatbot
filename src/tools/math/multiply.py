from langchain_core.tools import tool


@tool
def multiply(num_1, num_2):
    """
    Returns the product of num_1 and num_2
    """

    return num_1 * num_2