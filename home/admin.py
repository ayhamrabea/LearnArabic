from django.contrib import admin
from .models import Lesson , Said_question , Lesson_words
# Register your models here.


class Said_questionTablularInLine(admin.TabularInline):
    model = Said_question

class Said_wordsTablularInLine(admin.TabularInline):
    model = Lesson_words


class LessonAdmin(admin.ModelAdmin):
    inlines = [Said_questionTablularInLine , Said_wordsTablularInLine]
    class Meta:
        model = Lesson


admin.site.register(Lesson , LessonAdmin)
admin.site.register(Said_question)
admin.site.register(Lesson_words)