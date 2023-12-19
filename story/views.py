from django.shortcuts import render
from .models import Story , Parargraph
# Create your views here.


def index(request):

    story = Story.objects.all()

    context = {
        'stories' : story,
    }
    return render(request,'story.html',context)


def show_story(request,id):

    story = Story.objects.all()
    story_id = Story.objects.get(id=id)
    parargraph = Parargraph.objects.filter(story =story_id)

    context = {
        'stories' : story,
        'story_id':story_id,
        'parargraphs':parargraph,
    }

    return render(request,'story_detail.html',context)
