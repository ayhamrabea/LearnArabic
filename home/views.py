from django.shortcuts import render
from .models import Lesson , Said_question , Lesson_words
# Create your views here.


def index(request):

    lesson = Lesson.objects.all()

    context = {
        'lessons':lesson 
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

