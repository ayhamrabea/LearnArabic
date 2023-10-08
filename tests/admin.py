from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Quiz)

class Answeradmin(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [Answeradmin ]
    class Meta:
        model = Question



admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz_Said_question)
admin.site.register(Quiz_words)