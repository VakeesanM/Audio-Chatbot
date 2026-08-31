from langchain_core.tools import tool


@tool
def exponent(num, degree):
    """
    returns the product of inputed number to inputed degree

    args:
        num: The base Number  
        degree: The Degree of the exponent
    
    returns:
        num ** degree
    """

    return num ** degree