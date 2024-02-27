from django import forms
from . models import Todo
from django.forms import TextInput
class TodoForms(forms.ModelForm):
    class Meta:
        model=Todo
        fields =['title']
        widgets ={
                 'title':TextInput(attrs={
                 "type":"text",
                 "class":"form-control",
                 "placeholder":"enter your todo"
            })

        }