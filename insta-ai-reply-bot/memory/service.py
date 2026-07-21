from memory.database import get_session
from memory.models import Conversation



def save_conversation(
    user_id,
    message,
    response,
    response_type
):

    db = get_session()


    conversation = Conversation(

        user_id=user_id,

        user_message=message,

        bot_response=response,

        response_type=response_type

    )


    db.add(
        conversation
    )


    db.commit()


    db.close()