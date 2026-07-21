from openai import OpenAI
from openai import RateLimitError

from config import config


client = OpenAI(
    api_key=config.OPENAI_API_KEY
)


def chat_completion(
    system_prompt,
    user_message
):

    try:

        response = client.chat.completions.create(

            model=config.OPENAI_MODEL,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_message
                }

            ],

            temperature=0.7

        )

        return response.choices[0].message.content


    except RateLimitError:

        raise Exception(
            "OpenAI API quota unavailable. Check billing and API limits."
        )