from pydantic import BaseModel


class ReplyRequest(BaseModel):
    instagram_id: str
    message: str


class ReplyResponse(BaseModel):
    reply: str
    meme_url: str | None = None
    meme_title: str | None = None
    response_type: str