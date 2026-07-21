from typing import TypedDict


class AgentState(TypedDict):

    user_id: str
    message: str

    topic: str
    emotion: str
    keywords: list[str]
    humor_style: str
    requires_meme: bool

    meme_found: bool
    meme_url: str
    meme_title: str

    caption: str

    sarcasm_reply: str

    final_reply: str
    conversation_history: list