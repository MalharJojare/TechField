from openai import OpenAI

from config import config
from graph.state import AgentState


client = OpenAI(
    api_key=config.OPENAI_API_KEY
)


SYSTEM_PROMPT = """
You are a witty Instagram reply assistant.

Create sarcastic but friendly replies.

Rules:
- Keep it short.
- Make it playful, not offensive.
- Avoid being mean or insulting.
- Reply like a friend in an Instagram DM.
"""


def sarcasm_node(state: AgentState) -> AgentState:


    prompt = f"""
User message:

{state["message"]}

Topic:
{state["topic"]}

Emotion:
{state["emotion"]}

Create a sarcastic reply.
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


    reply = response.output_text.strip()


    state["sarcasm_reply"] = reply

    state["final_reply"] = reply


    return state