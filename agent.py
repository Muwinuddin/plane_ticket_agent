import os
from langchain_community.agent_toolkits.amadeus.toolkit import AmadeusToolkit
from langchain import LLMChain
from langchain_openai import ChatOpenAI  # use Groq client instead if needed

# load env
from dotenv import load_dotenv
load_dotenv()

# set up LLM (swap to your Groq Llama 3 client)
llm = ChatOpenAI(temperature=0)

# Amadeus tools
toolkit = AmadeusToolkit(llm=llm)
tools = toolkit.get_tools()

# build agent
from langchain.agents import create_openai_functions_agent
agent = create_openai_functions_agent(llm, tools)

