from crewai import Agent, Crew, Task, Process


def build_research_crew(topic: str, focus: str) -> Crew:
    researcher = Agent(
        role="Research Specialist",
        goal=f"Research '{topic}' and produce comprehensive findings",
        backstory=(
            "You are a meticulous research specialist with deep expertise in "
            "gathering and synthesizing information from diverse sources."
        ),
        verbose=True,
    )

    task = Task(
        description=(
            f"Research the following topic thoroughly.\n\n"
            f"Topic: {topic}\n"
            f"Focus: {focus}\n\n"
            "Produce a well-organized report covering key concepts, facts, "
            "examples, and insights. Be thorough and factual."
        ),
        expected_output=(
            "A detailed research report with clearly organized sections covering "
            "key findings, important facts, examples, and insights about the topic."
        ),
        agent=researcher,
    )

    return Crew(
        agents=[researcher],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )


def build_writing_crew(topic: str, research_notes: str) -> Crew:
    writer = Agent(
        role="Content Writer",
        goal="Write engaging, well-structured blog articles",
        backstory=(
            "You are an expert content writer who crafts compelling, informative "
            "articles that keep readers engaged from start to finish."
        ),
        verbose=True,
    )

    task = Task(
        description=(
            f"Write a comprehensive blog article based on the research below.\n\n"
            f"Topic: {topic}\n\n"
            f"Research Notes:\n{research_notes}\n\n"
            "Write a well-structured article with an introduction, clearly organized "
            "body sections, and a conclusion. Make it engaging and informative."
        ),
        expected_output=(
            "A complete, well-written blog article with a compelling introduction, "
            "structured body sections, and a strong conclusion."
        ),
        agent=writer,
    )

    return Crew(
        agents=[writer],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )


def build_review_crew(topic: str, draft: str) -> Crew:
    editor = Agent(
        role="Senior Content Editor",
        goal="Review and polish blog articles to publication quality",
        backstory=(
            "You are a seasoned editor with an eye for quality, clarity, and "
            "engagement. You improve articles while preserving the author's voice."
        ),
        verbose=True,
    )

    task = Task(
        description=(
            f"Review and improve the following blog article draft.\n\n"
            f"Topic: {topic}\n\n"
            f"Draft:\n{draft}\n\n"
            "Fix grammar, improve clarity, sharpen the opening hook, and ensure "
            "the article flows naturally. Produce the final, polished version."
        ),
        expected_output=(
            "A polished, publication-ready blog article that is clear, engaging, "
            "grammatically correct, and well-structured."
        ),
        agent=editor,
    )

    return Crew(
        agents=[editor],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )
