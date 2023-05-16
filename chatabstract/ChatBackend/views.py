from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import openai, os
import json
import re


def generate_prompt(operation) -> str:
    """generate prompts based on users' operations

    Args:
        operation (dict): a dict containing the user's operation in the following format
        operation = 
        {
            "text": "I eat food. I likes to eat food. I love hamburgers.",
            "start_index": 0,
            "end_index": 11,
            "comment": "Change to passive voice"
        }

    Returns:
        str: the prompt
    """
    prompt = "The original text is <" + str(operation["text"])+">. "
    sentence = str(operation["text"])[int(operation["start_index"]):int(operation["end_index"])]
    prompt += "For part <" + sentence + ">, " + "the user's comment is <" + operation["comment"] + ">."
    prompt += "Notice only the mentioned part should be changed. Your response should only contain a json object with two keys: text, sentence. Text means the whole text after the change, sentence means the part of the text that is after changing."
    return prompt


@csrf_exempt
def init(request): # stat conversation with gpt
    text = "I want you to help me modify a given text based on given user's comments. Your response should only contain a json object with two keys: text, sentence. Text means the whole text after the change, sentence means the part of the text that is changed. Respond a yes if you understand."
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"
    openai.api_key = "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"
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=2000,
        messages=[
            {"role": "user", "content": f"{text}"}
        ]
    )
    return HttpResponse("Start a new chatting.")


@csrf_exempt
def chat(request): # chat with gpt
    text = request.POST.get('text')
    print(text)
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"
    openai.api_key = "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"
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=2000,
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
    chat.save() # store the input , answer given by gpt and time to the database
    return HttpResponse(response)

    
@csrf_exempt
def respond_with_string(request): # get answer and return the answer with json form
    text = request.POST.get('text')
    print(text)
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"
    openai.api_key = "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"
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=2000,
        messages=[
            {"role": "user", "content": f"{text}"}
        ]
    )

    response = res.choices[0].message["content"]
    #print(response)
    #length_of_answer=len(response)
    chat = Chat.objects.create(
        text=text,
        gpt=response
    )
    chat.save()
    return HttpResponse(response)



@csrf_exempt
def respond_with_json(request): # get answer and return the answer with json form
    #text = request.POST.get('text')
    #start = request.POST.get('start_index')
    #end = request.POST.get('end_index')
    #comment = request.POST.get('comment')
    #operation = {
    #    "text": text,
    #    "start_index": start,
    #    "end_index": end,
    #    "comment": comment
    #}
    #prompt = generate_prompt(operation)
    operation=json.loads(request.body)
    prompt = generate_prompt(operation)
    #rint(text)
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"
    openai.api_key = "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"
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response = res.choices[0].message["content"]
    #print(response)
    #length_of_answer=len(response)
    #start_index=re.findall(r'"start_index": ([0-9]*?),', response)
    #end_index=re.findall(r'"end_index": ([0-9]*?),', response)
    #label=re.findall(r'"comment": (.*?),', response)

    #answer=json.dumps({'start': start_index, 'end': end_index , 'label':label}, sort_keys=True, indent=4, 
    #separators=(',', ': '))

    chat = Chat.objects.create(
        text=operation["text"],
        #prompt =prompt,
        gpt=response
    )
    chat.save()

    op= Operation.objects.create(
        text=operation["text"],
        pos_start=operation["start_index"],
        pos_end=operation["end_index"],
        comment=operation["comment"]
    )
    op.save()
    return HttpResponse(response)

