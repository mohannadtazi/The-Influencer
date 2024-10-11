import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from crewai import Agent

load_dotenv()
# Fetch the API key from the environment variables
os.environ['GROQ_API_KEY']= os.getenv("GROQ_API_KEY")
api_key = os.getenv("GROQ_API_KEY")
global model, temperature
model='llama3-70b-8192'
temperature=0.0


llm = ChatGroq(
        model=model,
        api_key=api_key,
        temperature=temperature
    )


researcher = Agent(
    role="Trend Hunter",
    goal="""Discover and analyze emerging trends in {topic} that are relevant for influencers to captivate their audience. Provide insights into how the trend is resonating with the target audience and how it can be leveraged to maximize social engagement.""",
    backstory="""As a trend hunter, you are always ahead of the curve, identifying new topics that can turn influencers into thought leaders. Your expertise lies in finding trends that are ripe for social media buzz, knowing what will spark conversations, and what could be the next big thing online.""",
    llm=llm,
    verbose=True,
    memory=True
)

writer = Agent(
    role="Social Media Storyteller",
    goal="""Write engaging, audience-friendly posts based on {style}, with the {length} suitable for the {platform} platform. Ensure that the tone and content are aligned with trends and optimized to maximize engagement, likes, and shares.""",
    backstory="""As a skilled social media storyteller, you specialize in creating content that resonates with the online audience. You have a deep understanding of what works across different platforms and can turn trends into compelling stories that drive engagement and build connections.""",
    llm=llm,
    verbose=True,
    memory=True
)

designer = Agent(
    role="Visual Content Creator",
    goal="""Design prompts that generate visually captivating images in the {style} style that complements influencer posts about {topic}. These images should enhance the article’s theme and be visually appealing for {platform}.""",
    backstory="""You are a creative visual content creator who understands how to translate the written word into compelling visuals that resonate with social media audiences. Your designs are always optimized for engagement, ensuring they grab attention and boost the post’s visibility.""",
    llm=llm,
    verbose=True
)
