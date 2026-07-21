from fastapi import FastAPI

from services.bot_service import process_message
from services.user_service import get_or_create_user
from app.schemas import ReplyRequest, ReplyResponse


app = FastAPI(
    title="Instagram AI Reply Bot"
)


@app.post("/reply", response_model=ReplyResponse)
def reply(data: ReplyRequest):

    user_id = get_or_create_user(data.instagram_id)

    response = process_message(
        user_id=str(user_id),
        message=data.message
    )

    return response