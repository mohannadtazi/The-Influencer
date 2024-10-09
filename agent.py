import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from crewai import Agent

load_dotenv()
# Fetch the API key from the environment variables
# Fetch the API key from the environment variables
os.environ['GROQ_API_KEY']= os.getenv("GROQ_API_KEY")
api_key = os.getenv("GROQ_API_KEY")
model="groq/llama3-8b-8192"


llm = ChatGroq(
    model=model,
    api_key=api_key,
    temperature=0.5,  
)


researcher= Agent(
role="Senior Researcher",
goal="""Uncover groundbreaking topics in {topic}""", 
backstory="""Driven by curiosity, you are at the forefront of Innovation sharing knowledge and news that would change the world""",
llm=llm,
verbose=True,memory=True,)


writer= Agent(
role="Writer",
goal="""Narrate compelling stories following the style: {style}, and it should be {length}, addapted for {platform} platform""", 
backstory="""Your expertise lies in breaking down complex topics into simpler and digestable knowledge, you specialize in captivativing audience attention with your writing and create engaging narratives and stories""",
llm=llm,
verbose=True,memory=True)