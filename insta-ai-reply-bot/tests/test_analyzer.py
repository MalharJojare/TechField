from agents.analyzer import analyzer_node

state = {
    "user_id": "123",
    "message": "My manager scheduled another useless meeting",

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

result = analyzer_node(state)

print(result)