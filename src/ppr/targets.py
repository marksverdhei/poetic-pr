import json
import os
import shlex
import webbrowser

from . import prompt


def auth():
    """
    Specify either username and password, or access token
    """
    HOME = os.getenv("HOME", ".")
    if not os.path.exists(f"{HOME}/.cache"):
        os.mkdir(f"{HOME}/.cache")

    if not os.path.exists(f"{HOME}/.cache/ppr"):
        os.mkdir(f"{HOME}/.cache/ppr")

    print(
        "Opening https://chat.openai.com/api/auth/session in your default browser",
        "Copy the content and paste it in the terminal.",
        sep="\n",
    )
    webbrowser.open("https://chat.openai.com/api/auth/session")
    json_object = input()

    try:
        auth_json = json.loads(json_object)
    except Exception:
        print("Failed to parse data. Make sure to copy the entire string.")
        print("Otherwise, please submit an issue to our github repository: https://github.com/marksverdhei/poetic-pr")
        return 1

    if "accessToken" not in auth_json:
        print("Access token not found. Make sure to copy the entire string.")
        print("Otherwise, please submit an issue to our github repository: https://github.com/marksverdhei/poetic-pr")
        return 1

    with open(f"{HOME}/.cache/ppr/access_token", "w+") as f:
        f.write(auth_json["accessToken"])

    print("Authorization successful!")


def comment(number):
    """Comments on a pull request"""
    answer = prompt.generate_poem()
    print("Generated poem:")
    print(answer)
    quoted_answer = shlex.quote(answer)
    os.system(f"gh pr comment {number} -b {quoted_answer}")


def pr(title):
    """Creates a pull request with the pome as its content"""
    # TODO: get prompt from git diff
    poem = prompt.generate_poem()
    quoted_answer = shlex.quote(poem)
    os.system(f"gh pr create --title {title} -b {quoted_answer}")


def ready(args):
    """Converts a pull request to ready with a poem requesting for a review"""
    pass
