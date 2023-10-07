from django.http import HttpResponse, JsonResponse
from django.shortcuts import render ,redirect
from .models import *
import random
# Create your views here.

def home(request):
    quiz = Quiz.objects.all()

    context = {
        'quizes' : quiz
    }

    return render(request,'home.html' , context)



def detail_page(request,id):

    quiz = Quiz.objects.all()
    quiz_id = Quiz.objects.get(id=id)
    questions = Question.objects.filter(quiz=quiz_id)

    



    context = {
        'quizes':quiz,
        'quiz_id':quiz_id,
        'questions':questions,

    }

    return render(request,'detail_quiz.html',context)



def get_quize(request ,id):

    try:
        quiz_id = Quiz.objects.get(id=id)
        question_objs = Question.objects.filter(quiz=quiz_id)

        question_objs = list(question_objs)
        data=[]
        random.shuffle(question_objs)


        for question_obj in question_objs:
            data.append({
                'quiz':question_obj.quiz.quiz_name,
                'question':question_obj.question,
                'marks':question_obj.marks,
                'answers':question_obj.get_answers()
                })
            


        payload = {'status': True , 'data':data}
        return JsonResponse(payload)
        
    except Exception as e:
        print(e)
    return HttpResponse("something went wrong")


    