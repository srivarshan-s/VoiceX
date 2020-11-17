from django.shortcuts import render
from gtts import gTTS
import os

def insert(q, x) :
    q.append(x)
    q.append(' ')

def home(request) :
    text_ = request.POST.get('textbox', 'No text entered')
    text_ = text_.split()
    queue = []
    for i in text_ :
        insert (queue, i)
    mytext = ''
    while queue != []:
        mytext += queue.pop(0)
    language = request.POST.get('lang', 'en-us')
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("static/audio/mytext.mp3")
    print(mytext)
    return render(request, 'voicex/home.html')

def text_editor(request) :
    return render(request, 'voicex/text_editor.html')

def recommend(request) :
    return render(request, 'voicex/recommend.html')
