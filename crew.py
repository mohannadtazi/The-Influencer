from crewai import Crew
from task import research_task,write_task
from agent import researcher,writer

crew= Crew(
agents=[researcher,writer],
tasks=[research_task,write_task]
)
