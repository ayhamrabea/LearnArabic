from django import forms
from .models import modelcontact


class contactform(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'الأسم' , 'class':'form-control bg-dark text-white border-0' ,'style':'height: 55px; font-size: 20px;' }))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':' بريدك الألكتروني' , 'class':'form-control bg-dark text-white border-0' ,'style':'height: 55px; font-size: 20px;' }))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'الموضوع' , 'class':'form-control bg-dark text-white border-0' ,'style':'height: 55px; font-size: 20px;' }))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'الرسالة' , 'class':'form-control bg-dark text-white border-0' ,'style':'height: 55px; font-size: 20px;' }))

    class Meta:

        model = modelcontact
        fields = '__all__'
