from crewai import Task
from tools import tool
from agent import researcher, writer, designer

# Define the research task first
research_task = Task(
    description="""Identify the next big trend in {topic}. Focus on identifying pros and cons and the overall narrative. Your final report should clearly articulate the key points, its market opportunities, and potential risks.""",
    expected_output="A comprehensive 3 paragraphs long report on the latest AI trends.",
    tools=[tool],
    agent=researcher
)

# Then define the write task, making sure to use the correct context
write_task = Task(
    description="""Compose an insightful article based on the research_task results. Focus on the latest trends and how it's impacting the industry. This article should be in a {style} style, and {length} length adapted for {platform} platform.""",
    expected_output="A 4 paragraph article following the {style} style, and {length} length [keep in mind short means 5 lines] adapted for {platform} platform formatted as markdown.",
    agent=writer,
    async_execution=False
)

# Then define the Design task
design_task = Task(
    description="""Craft a prompt to genarte a visually appealing image in the {style} style to accompany the article. The image should capture the essence of the article about {topic} and be suitable for {platform} platform.""",
    expected_output="A really short prompt to generate visually appealing image that captures the essence of the article and is suitable for {platform} platform. Don't include any text exept the prompt.",
    agent=designer,
)
