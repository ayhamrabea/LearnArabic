import os
from django.shortcuts import render , redirect
from .models import Lesson , Said_question , Lesson_words , People_Ask
import random
import pyttsx3

# Create your views here.


def index(request):

    

    lesson = Lesson.objects.all().order_by('numper_of_lesson')
    
    # People_Ask model
    questions = People_Ask.objects.all()
    questions_objs = list(questions)
    random.shuffle(questions_objs)

    

    context = {
        'lessons':lesson,
        'questions':questions_objs,
    }

    return render(request,'index.html',context)


# def say_text(request):
#     value = request.GET['inp']
#     TTS = gTTS(text=value, lang='en-uk')
#     # obj = pyttsx3.init()
#     # obj.say(value)
#     # obj.runAndWait()
#     os.system("start voice.mp3")

#     return redirect('/')


def detail_page(request,id):

    lesson = Lesson.objects.all()
    lesson_id = Lesson.objects.get(id=id)
    said_questions = Said_question.objects.filter(lesson=lesson_id)
    words = Lesson_words.objects.filter(lesson=lesson_id)   


    context = {
        'lessons':lesson,
        'lesson_id':lesson_id,
        'said_questions':said_questions,
        'words':words,
    }

    return render(request,'detail.html',context)

