import openai
from decouple import config


def openai_response(message: str) -> str:
    try:
        openai.api_key = config('OPEN_AI_KEY')
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = message,
            temperature = 0.3,
            max_tokens = 1024,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0,
        )
        
        return response.get("choices")[0]["text"]
    except openai.error.OpenAIError as e:
        print(e.http_status)
        print(e.error)
        if (str(e.error) == 'None'): e.error = '生不出來'
        return e.error


def openai_generalIMG(message: str) -> str:
    try:
        response = openai.Image.create(
            prompt=message,
            n=1,
            size="1024x1024"
        )
    
        return response['data'][0]['url']
    except openai.error.OpenAIError as e:
        print(e.http_status)
        print(e.error)
        if (str(e.error) == 'None'): e.error = '生不出來'
        return e.error