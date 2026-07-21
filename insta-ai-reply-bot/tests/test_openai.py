from services.openai_service import chat_completion


result = chat_completion(
    "You are a helpful assistant",
    "Say hello"
)


print(result)