import cohere
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CO_API_KEY")
co = cohere.Client(api_key)

# Keep track of historical responses
chat_history = []
max_turns = 10
def chatboxAPI(message):
    # get user input
    # message = input("Send the model a message: ")


    #generate chat response
    response = co.chat(
        message=message, 
        model="command", 
        temperature=0.3,
        chat_history=chat_history
    )


    # add message and answer to chat history
    user_message = {"role": "USER", "text": message}
    bot_message = {"role": "CHATBOT", "text": response.text}
    chat_history.append(user_message)
    chat_history.append(bot_message)

    # TODO: change the # of max_turns
    print(response.text)
    return response.text
# chatboxAPI("what is today data")