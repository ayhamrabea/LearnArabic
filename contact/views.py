from django.shortcuts import render , redirect
from django.urls import reverse
from .models import modelcontact
from .forms import contactform
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def contact_page(request):
    form = contactform()
    if request.method == 'POST':
        the_sender = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            # send_mail(
            #     subject,
            #     message,
            #     the_sender,
            #     ["ayhamstudy05@gmail.com" ],
            # )
            return redirect('home')
    else:
        form = contactform()




    context ={
        'form': form,
    }
    return render(request,'contact.html',context)