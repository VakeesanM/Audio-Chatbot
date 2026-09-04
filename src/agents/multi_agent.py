from deepagents import create_deep_agent
from src.agents.sub_agents.math_agent import create_math_agent
from src.agents.sub_agents.web_agent import create_web_agent
from langchain.agents.middleware import SummarizationMiddleware, PIIMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI

def create_multi_agent_chatbot():
    model = ChatOpenAI(model='gpt-4o-mini', temp=0.8),
    memory = InMemorySaver()
    summary_ware = SummarizationMiddleware(
        model = model,
        trigger= ('tokens', 2500),
        keep = ('messages', 10)
    )

    system_prompt = """ 
        You are a AI Chatbot, whose purpose is to help and talk with the user.
        ### TASKS
        * Answer the user questions with you knowledge
        * Never Lie to the user
        * Help them to best of your ability

        ### Important
        * Keep responses short
        * NO filbustering
        * NO inapproiate language or curse words
        * State when you don't something
        * Use the tools given to you if you think they are helpful to user's current query

        """

    agent = create_deep_agent(
        model = model,
        subagents= [create_math_agent(), create_web_agent()],
        checkpointer=memory,
        middleware= [summary_ware,
                     PIIMiddleware('credit_card'),
                     PIIMiddleware('ip'),
                     PIIMiddleware('mac_address')],
        systemprompt= system_prompt)

    return agent
    