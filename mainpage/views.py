from django.shortcuts import render
from . import models

def mainpage_all(request):
    instructor = models.Instructor.objects.all()
    return render(request, 'index.html', {'instructor': instructor})
# Create your views here.

def courses(request):
    course = models.Course.objects.all()
    return render(request, 'index.html', {'course': course})

def blogs(request):
    blogs = models.Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def traffic_laws(request):
    traffic_laws = models.Traffic_Law.objects.all()
    return render(request, 'index.html', {'traffic_laws': traffic_laws})