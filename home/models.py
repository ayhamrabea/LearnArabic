from django.db import models
from tests.models import Quiz

# Create your models here.


class Lesson(models.Model):

    numper_of_lesson = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    leavel = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=False, blank=True, null=True)
    quiz = models.ForeignKey(Quiz,related_name='Lesson_Quiz', on_delete=models.CASCADE , default=1)
    

    class Meta:

        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.name 


class Said_question(models.Model):

    lesson = models.ForeignKey( Lesson ,on_delete=models.CASCADE, blank=True, null=True)
    question = models.CharField(max_length=100, blank=True, null=True)
    said_description = models.TextField( blank=True, null=True)


    class Meta:
        verbose_name = ("Said_question")
        verbose_name_plural = ("Said_questions")

    def __str__(self):
        return self.question



class Lesson_words(models.Model):

    lesson = models.ForeignKey( Lesson ,on_delete=models.CASCADE, blank=True, null=True)
    lesson_word_id = models.IntegerField(default=99, blank=True, null=True)
    word_AR = models.CharField( max_length=50, blank=True, null=True)
    word_RU = models.CharField( max_length=50, blank=True, null=True)
    # audio_file = models.FileField( upload_to =  'uploads/' , blank=True, null=True)


    class Meta:
        verbose_name = ("Lesson_words")
        verbose_name_plural = ("Lesson_wordss")

    def __str__(self):
        return self.word_AR
    


class People_Ask(models.Model):

    question = models.CharField(max_length=250)
    answer = models.TextField()
    class Meta:

        verbose_name = 'People_Ask'
        verbose_name_plural = 'People_Asks'

    def __str__(self):
        return self.question

