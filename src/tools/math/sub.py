from langchain_core.tools import tool


@tool
def sub(num_1, num_2):
    """
    Returns the num_1 - num_2.
    
    """

    return num_1-num_2