# services/bot_service.py

from graph.workflow import build_workflow


workflow = build_workflow()


def process_message(
    user_id: str,
    message: str
):

    state = {

        "user_id": user_id,

        "message": message,

        "conversation_history": [],

        "topic": "",

        "emotion": "",

        "keywords": [],

        "humor_style": "",

        "requires_meme": False,

        "meme_found": False,

        "meme_url": "",

        "meme_title": "",

        "caption": "",

        "sarcasm_reply": "",

        "final_reply": ""

    }


    result = workflow.invoke(state)


    return {

        "reply": result["final_reply"],

        "meme_url": result.get("meme_url"),

        "meme_title": result.get("meme_title"),

        "response_type": (
            "meme"
            if result.get("meme_found")
            else "sarcasm"
        )

    }