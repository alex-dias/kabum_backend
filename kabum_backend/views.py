from django.http import HttpResponse
from django.shortcuts import render
from . import forms

def home(request):
    form = forms.usersClass()
    return render(request, 'home.html', {'form': form, 'test2': form.test2})
