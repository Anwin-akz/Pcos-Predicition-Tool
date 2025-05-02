from django.shortcuts import render
import pickle
import json
import random

from flask_session import Session
from flask import session

# Load the trained model and vectorizer
with open('C:/Users/User/Desktop/ChatBot/ChatBot/venv/chatbot/model/chatbot_model.pkl', 'rb') as f:
    best_model = pickle.load(f)
with open('C:/Users/User/Desktop/ChatBot/ChatBot/venv/chatbot/model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load the intents data
with open('C:/Users/User/Desktop/ChatBot/ChatBot/venv/chatbot/dataset/career_guidance.json', 'r') as f:
    intents = json.load(f)

def chatbot_response(user_input):
    input_text = vectorizer.transform([user_input])
    predicted_intent = best_model.predict(input_text)[0]

    for intent in intents['intents']:
        if intent['tag'] == predicted_intent:
            response = random.choice(intent['responses'])
            break

    return response


from django.http import HttpResponse

from django.http import JsonResponse



def chats(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        response_text = chatbot_response(user_input)
        
        return JsonResponse({'response_text': response_text})
    else:
        return render(request, 'chat.html')
    