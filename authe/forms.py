from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class creatuserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':' your name' , 'class':' form-control  bg-light px-4 mb-3' ,'style':"height: 55px"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'your email' , 'class':' form-control  bg-light px-4 mb-3' ,'style':"height: 55px"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'your password' , 'class':' form-control  bg-light px-4 mb-3' ,'style':"height: 55px"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'your password' , 'class':' form-control  bg-light px-4 mb-3' ,'style':"height: 55px"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class loginForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':' your name' , 'class':' form-control  bg-light px-4 mb-3' ,'style':"height: 55px"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'your password' , 'class':' form-control  bg-light px-4 mb-3' ,'style':"height: 55px"}))
    
    class Meta:
        model = User
        fields = ['username','password']


# class contactform(forms.ModelForm):
    
#     name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'الأسم' , 'class':'form-control bg-dark text-white border-0' ,'style':'height: 55px; font-size: 20px;' }))
#     email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':' بريدك الألكتروني' , 'class':'form-control bg-dark text-white border-0' ,'style':'height: 55px; font-size: 20px;' }))
#     subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'الموضوع' , 'class':'form-control bg-dark text-white border-0' ,'style':'height: 55px; font-size: 20px;' }))
#     message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'الرسالة' , 'class':'form-control bg-dark text-white border-0' ,'style':'height: 55px; font-size: 20px;' }))

#     class Meta:

#         model = modelcontact
#         fields = '__all__'
