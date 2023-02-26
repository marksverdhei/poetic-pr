import os

from revChatGPT.V1 import Chatbot

HOME = os.getenv("HOME", ".")
ACCESS_TOKEN_PATH = f"{HOME}/.cache/ppr/access_token"


def auth_chatbot():
    if not os.path.exists(ACCESS_TOKEN_PATH):
        print("No auth token found")
        raise Exception()

    with open(ACCESS_TOKEN_PATH) as f:
        token = f.read()

    chatbot = Chatbot({"access_token": token})
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
