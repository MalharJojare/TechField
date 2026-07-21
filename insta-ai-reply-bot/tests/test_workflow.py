from graph.workflow import build_workflow


app = build_workflow()


state = {

    "user_id": "37e5754d-a352-4df7-8867-6686b8a588f3",

    "message": "My manager scheduled another useless meeting",
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


result = app.invoke(state)


print("\nFINAL RESULT\n")

print(result)