from django.contrib import admin
from .models import Story , Parargraph
# Register your models here.


class ParargraphTablularInLine(admin.TabularInline):
    model = Parargraph




class StoryAdmin(admin.ModelAdmin):
    inlines = [ParargraphTablularInLine ]
    class Meta:
        model = Story


admin.site.register(Story , StoryAdmin)
admin.site.register(Parargraph)
