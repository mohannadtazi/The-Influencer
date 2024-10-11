from crewai import Task
from tools import tool
from agent import researcher, writer, designer

# Task for discovering the next big trend
research_task = Task(
    description="""Identify the emerging trend within {topic} that would be highly relevant for social media influencers. Focus on key talking points, benefits, and potential drawbacks. The final report should highlight why this trend is gaining momentum and its potential impact on the audience.""",
    expected_output="A report detailing the key points of the trend, including its appeal to social media audiences, its market potential, and possible risks.",
    tools=[tool],
    agent=researcher
)

# Task to write an engaging article for social media
write_task = Task(
    description="""Based on the results from the research_task, craft an engaging post highlighting the current trend. The post should be tailored to resonate with your audience and be written in a {style} style and {length} length, specifically adapted for the {platform} platform.""",
    expected_output="A social media post formatted in markdown with {style} style, {length} length (short means 5 lines..), focusing on the trend's relevance and engaging the target audience on the {platform} platform.",
    agent=writer,
    async_execution=False
)


# Task for generating a visual prompt
design_task = Task(
    description="""Create a prompt for generating a visually striking image in {style} that complements the article. The image should effectively convey the theme of the trend and be optimized for the {platform} platform, aligning with the content’s tone and message.""",
    expected_output="A concise image prompt that captures the essence of the article and fits well with the {platform} platform’s style. Only provide the image prompt without any additional text.",
    agent=designer,
)
