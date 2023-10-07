from django.db import models
import uuid
import random
# Create your models here.

class Quiz(models.Model):
    quiz_name = models.CharField( max_length=150)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField( max_length=250)
    marks = models.IntegerField(default=5)
    discrption = models.TextField()
    class Meta:

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


    def __str__(self):
        return self.question
    
    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question=self))
        random.shuffle(answer_objs)
        data = []
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct':answer_obj.is_correct
            })
        return data




class Answer(models.Model):

    question = models.ForeignKey(Question,related_name='question_Answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=150)
    is_correct = models.BooleanField(default=False)

    class Meta:

        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


    def __str__(self):
        return self.answer


