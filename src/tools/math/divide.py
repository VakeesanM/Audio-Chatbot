from langchain_core.tools import tool


@tool
def divide(num_1, num_2):
    """
    Returns the num_1/num2


    args:
        num_1: The Number being divided by num_2
        num_2: The Number dividing num1


    Example:
        if num_1 = 15 and num_2 = 5,
        then divide(num_1, num_2) would return 3
    """

    return num_1/num_2