from services.bot_service import process_message


response = process_message(

    "37e5754d-a352-4df7-8867-6686b8a588f3",

    "My manager scheduled another useless meeting"

)


print("\nBOT RESPONSE\n")

print(response)