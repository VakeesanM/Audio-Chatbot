from langchain_core.tools import tool


@tool
def root(num, degree):
    """
    returns the root of inputed number to inputed degree

    args:
        num: The Number to root
        degree: The Degree of the root
    
    returns:
        num ** (1/degree)
    """

    return num ** (1/degree)