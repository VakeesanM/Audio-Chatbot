from tools.math.add import add
from tools.math.sub import sub
from tools.math.multiply import multiply
from tools.math.divide import divide
from tools.math.exponent import exponent
from tools.math.root import root
# The Config for the Math Agent


prompt = """
    You are a mathematics who can solve math problems.
   
    #Important
    * Don't show your work
    * Give only your final answer
    """

def math_agent_config(model):
    math_agent = {
        "name:": "math-agent",
        "description" : "Used to solve math problems",
        "system_prompt": prompt,
        "tools": [add, sub, multiply, divide, exponent, root],
        "model": model
        
    }

    return math_agent