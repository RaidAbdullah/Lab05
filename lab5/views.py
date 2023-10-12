from django.shortcuts import render , redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect



# Create your views here.
class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

people = []

    
def index(request):
    return render(request,'lab5/list.html',{'people':people})


class PersonForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username1 = form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            person = Person(username1,password1)
            people.append(person)
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'Lab5/add.html', {'form': PersonForm()})

