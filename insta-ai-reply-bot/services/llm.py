from openai import OpenAI
from config import config


client = OpenAI(
    api_key=config.OPENAI_API_KEY
)


def ask_llm(
    system_prompt,
    user_message
):

    response = client.chat.completions.create(

        model=config.OPENAI_MODEL,

        messages=[

            {
                "role":"system",
                "content":system_prompt
            },

            {
                "role":"user",
                "content":user_message
            }

        ],

        temperature=0.8
    )


    return (
        response
        .choices[0]
        .message
        .content
    )