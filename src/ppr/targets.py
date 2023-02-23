import os
import shlex

from . import prompt


def auth(
    username=None,
    password=None,
    access_token=None,
):
    """
    Specify either username and password, or access token
    """
    if username is not None and password is not None:
        credentials = {
            "username": username,
            "password": password,
        }
    elif access_token is not None:
        credentials = {
            "access_token": access_token,
        }
    else:
        raise ValueError("You must pass passwords")

    for k, v in credentials.items():
        os.environ["PPR_" + k.upper()] = v


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
