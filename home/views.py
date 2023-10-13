from django.shortcuts import render
from .models import Lesson , Said_question , Lesson_words , People_Ask
import random

# Create your views here.


def index(request):

    lesson = Lesson.objects.all()

    # People_Ask model
    questions = People_Ask.objects.all()
    questions_objs = list(questions)
    random.shuffle(questions_objs)


    context = {
        'lessons':lesson,
        'questions':questions_objs, 
    }

    return render(request,'index.html',context)

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

