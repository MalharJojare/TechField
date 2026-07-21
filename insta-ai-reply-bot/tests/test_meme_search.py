from agents.meme_search import meme_search_node


state = {

    "user_id": "1",

    "message": "My manager scheduled another useless meeting",

    "topic": "work",

    "emotion": "frustrated",

    "keywords": [

        "meeting",

        "office",

        "corporate"

    ],

    "humor_style": "sarcastic",

    "requires_meme": True,

    "meme_found": False,

    "meme_url": "",

    "meme_title": "",

    "caption": "",

    "sarcasm_reply": "",

    "final_reply": ""

}

result = meme_search_node(state)

print(result)