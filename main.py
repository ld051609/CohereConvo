import cohere
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CO_API_KEY")
co = cohere.Client(api_key)
# message = input("Can you summarize the text for me: ")
# CONVERSATION_ID='previous_id'
# response = co.chat_stream(
# 	message=message, 
# 	model="command", 
# 	temperature=0.3,
#     conversation_id=CONVERSATION_ID
# )

# # print out the stream response
# for event in response:
#     if event.event_type == "text-generation":
#         print(event.text, end='')


# Keep track of historical responses
chat_history = []
max_turns = 10
for _ in range(max_turns):
    # get user input
    message = input("Send the model a message: ")

    # Initialize answer for each turn
    answer = ""

    #generate chat response
    response = co.chat_stream(
        message=message, 
        model="command", 
        temperature=0.3,
        chat_history=chat_history
    )
    for event in response:
        if event.event_type == "text-generation":
            answer+= event.text
            print(event.text, end='')
    
    print("\n")
    # add message and answer to chat history
    user_message = {"role": "USER", "text": message}
    bot_message = {"role": "CHATBOT", "text": answer}
    chat_history.append(user_message)
    chat_history.append(bot_message)

    # TODO: change the # of max_turns