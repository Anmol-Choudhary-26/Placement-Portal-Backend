from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI
import os
from django.shortcuts import render

client = OpenAI( api_key=os.environ.get("OPENAI_API_KEY"),)


# Set your OpenAI API key here

@api_view(['POST'])
def chat_api(request):
    message = request.data.get('message', '')
    print(OpenAI)
    if not message:
        return Response({'error': 'Message parameter is required'}, status=400)

    try:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": "You are a helpful assistant."},
             {"role": "user", "content": "Hello!"}
         ]
        )
        print(completion.choices[0].message)
        return Response({'message': completion.choices[0].message})
    except Exception as e:
        print(str(e))
        return Response({'error': str(e)}, status=500)



def index(request):
    return render(request, 'chat/index.html')