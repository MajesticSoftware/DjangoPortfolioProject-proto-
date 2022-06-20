
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def timelapse(request):
    return render(request, 'timelapse.html')

def ai_projects(request):
    return render(request, 'ai_projects.html')