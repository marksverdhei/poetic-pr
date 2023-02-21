import json
from revChatGPT.V1 import Chatbot

# with open("/home/.config/revChatGPT/config.json") as f:
#     config = json.load(f)


def main():
    chatbot = Chatbot(
        {"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrc3ZlcmRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJOTyJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItM1FVaVdOTDdTS0NQSlBxdnp1eGNYelVmIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDEzMzQ0NTk4MjAzMTIzODYwNiIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NzYzOTcyMjcsImV4cCI6MTY3NzYwNjgyNywiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvZmZsaW5lX2FjY2VzcyJ9.go5ttrKzbrCyjMjqkYJEkFGBSBYgrLz51PVn3GKskd3T1dRbz2LSf8JkLWrgwJOkGjmtuXvRYUUzZiFjWcW8mRBFC0iyLgQrTfhQQA2eTm0Zj5SINVHPd18MKHSonKkGOX-Ey6fq4_qiMpv-3F9W5IlkTmC7FYB9rJg8xqF5yGxY4IrtMTqNeGmdyHXLD8vlQ5qS6Pjhjfkz-_roSMUH9V1EchusckIQ6GBt41vlX9W1oGhDEjr7sttiWWh3wXvLqo7pMyXmkRh3hVSlTsnkIsMaeS0jrU2KYwqbo0t_1-PPHDYUjBZCAa6WjMfRWdhydihmhaB8ROPCfZSi09-Qrw"}
    )

    starter_prompt = """
    Please write a rhyming poem about writing a pull request and asking to review it.
    """
    data_iterator = chatbot.ask(starter_prompt)
    for i in data_iterator:
        answer = i["message"]

    
    print(answer)


if __name__ == "__main__":
    main()