from openai import OpenAI

from config import config
from graph.state import AgentState


client = OpenAI(
    api_key=config.OPENAI_API_KEY
)


SYSTEM_PROMPT = """
You are an Instagram meme caption writer.

Your job is to create a short funny caption
for a meme reply.

Rules:
- Keep it under 15 words.
- Make it suitable for an Instagram DM.
- Match the user's emotion and situation.
- Do not explain the joke.
- Do not use hashtags.
"""


def caption_node(state: AgentState) -> AgentState:

    prompt = f"""
User message:
{state["message"]}

Detected topic:
{state["topic"]}

Emotion:
{state["emotion"]}

Meme selected:
{state["meme_title"]}

Create a funny caption for this meme.
"""


    response = client.responses.create(

        model=config.OPENAI_MODEL,

        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

    )


    caption = response.output_text.strip()


    state["caption"] = caption

    state["final_reply"] = caption


    return state