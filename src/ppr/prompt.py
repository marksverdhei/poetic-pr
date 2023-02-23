from revChatGPT.V1 import Chatbot
import os


def auth_chatbot():
    token = os.getenv("PPR_ACCESS_TOKEN", None)
    chatbot = Chatbot(
        {
            "access_token": token
        }
    )
    return chatbot



def generate_poem() -> str:
    starter_prompt = """
    Please write a single-paragraph rhyming poem about writing a pull request and asking to review it.
    """
    chatbot = auth_chatbot()
    data_iterator = chatbot.ask(starter_prompt)
    
    for i in data_iterator:
        answer = i["message"]
    
    return answer

