from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from django.urls import reverse
import os

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Home': reverse('home'),
        'Show current time': reverse('time'),
        'Show contents of working directory': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    msg = f'Current time: {current_time}'
    return HttpResponse(msg)

def workdir_view(request):
    files = os.listdir('.')
    file_list = '\n'.join(files)
    return HttpResponse(file_list)

