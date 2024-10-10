from crewai import Crew
from task import research_task,write_task,design_task
from agent import researcher,writer,designer

crew_image= Crew(
agents=[designer],
tasks=[design_task]
)

crew= Crew(
agents=[researcher,writer],
tasks=[research_task,write_task]
)
