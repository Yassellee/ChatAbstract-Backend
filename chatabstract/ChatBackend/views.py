from .models import *
import openai, os


def init(request): # stat conversation with gpt
    text = "I want you to act as my academic writing mentor and polish my essay according to my instructions."
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"
    openai.api_key = "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"
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=10000,
        messages=[
            {"role": "user", "content": f"{text}"}
        ]
    )



def chat(request): # chat with gpt
    text = request.POST.get('text')
    print(text)
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"
    openai.api_key = "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"
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=10000,
        messages=[
            {"role": "user", "content": f"{text}"}
        ]
    )

    response = res.choices[0].message["content"]
    print(response)

    chat = Chat.objects.create(
        text=text,
        gpt=response
    )

