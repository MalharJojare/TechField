from memory.service import get_session
from memory.models import Conversation


def get_conversation_history(user_id):

    db = get_session()

    try:

        conversations = (
            db.query(Conversation)
            .filter(Conversation.user_id == user_id)
            .order_by(Conversation.created_at.desc())
            .limit(10)
            .all()
        )


        history = []


        for item in conversations:

            history.append(
                {
                    "role": "user",
                    "content": item.user_message
                }
            )


            history.append(
                {
                    "role": "assistant",
                    "content": item.bot_response
                }
            )


        return history


    finally:

        db.close()

def save_conversation(
    user_id: str,
    message: str,
    response: str
):

    db = get_session()

    try:

        conversation = Conversation(

            user_id=user_id,

            user_message=message,

            bot_response=response,

            response_type="text"

        )


        db.add(conversation)

        db.commit()


    finally:

        db.close()