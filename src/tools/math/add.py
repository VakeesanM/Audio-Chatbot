from langchain_core.tools import tool


@tool
def add(num_1, num_2):
    """
    Returns the sum of num_1 and num2
    """

    return num_1 + num_2