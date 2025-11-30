from django.contrib import admin
from django.shortcuts import render



def home(request):
    return render(request, 'home-blogs.html')
