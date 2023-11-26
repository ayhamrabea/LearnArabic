from django.shortcuts import render , redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .forms import creatuserForm , loginForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.


# def form_invalid(self, form):
#         messages.error(self.request,'Invalid username or password')
#         return self.render_to_response(self.get_context_data(form=form))


def singup_page(request):
    if request.method == 'POST':
        form = creatuserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            # user = form.cleaned_data.get('username')
            # messages.success(request,'Account was created ' + user)
            return redirect('index')
        else:
            form = creatuserForm()
            messages.error(request ,'username or password not correct')
    else:
        form = creatuserForm()
    return render(request,'singup.html',{'form':form})     



def login_page(request):
    if request.method == "POST":
        form = loginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, ' username or password is incorrect ')
    else:
        form = loginForm()

    return render(request,'login.html',{'form':form})     



def logout_page(request):

    logout(request)
    return redirect('login')



