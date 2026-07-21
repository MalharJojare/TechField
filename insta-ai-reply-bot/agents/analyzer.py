from pydantic import BaseModel
from openai import OpenAI

from config import config
from graph.state import AgentState


client = OpenAI(
    api_key=config.OPENAI_API_KEY
)


class Analysis(BaseModel):
    topic: str
    emotion: str
    keywords: list[str]
    humor_style: str
    requires_meme: bool


SYSTEM_PROMPT = """
You are an AI Message Analyzer for an Instagram Meme Reply Bot.

Your job is to understand the user's message.

Extract:

1. topic
2. emotion
3. 3-5 meme search keywords
4. humor_style
5. requires_meme

Rules:

- Return structured data only.
- Keywords should be useful for searching GIFs/memes.
- If the message is serious (death, illness, emergency, mental health, etc.), set requires_meme to false.
- Otherwise requires_meme should usually be true.
"""


def analyzer_node(state: AgentState) -> AgentState:

    message = state["message"]

    response = client.responses.parse(
        model=config.OPENAI_MODEL,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
        text_format=Analysis,
    )

    analysis = response.output_parsed

    state["topic"] = analysis.topic
    state["emotion"] = analysis.emotion
    state["keywords"] = analysis.keywords
    state["humor_style"] = analysis.humor_style
    state["requires_meme"] = analysis.requires_meme

    return state