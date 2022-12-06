from django.shortcuts import render
from . import models

def mainpage_all(request):
    instructor = models.Instructor.objects.all()
    course = models.Course.objects.all()
    blogs = models.Blog.objects.all()
    traffic_laws = models.Traffic_Law.objects.all()
    context = {
        'instructor':instructor,
        'course': course,
        'blogs': blogs,
        'traffic_laws': traffic_laws,
    }
    return render(request, 'index.html', context)
# Create your views here.

def extended_info(request, id):
    instructor = models.Instructor.objects.get(id=id)
    course = models.Course.objects.get(id=id)
    blogs = models.Blog.objects.get(id=id)
    traffic_laws = models.Traffic_Law.objects.get(id=id)
    context = {
        'instructor': instructor,
        'course': course,
        'blogs': blogs,
        'traffic_laws': traffic_laws,
    }
    return render(request, 'extended_info.html', context)
# def courses(request):
#     course = models.Course.objects.all()
#     return render(request, 'index.html', {'course': course})
#
# def blogs(request):
#     blogs = models.Blog.objects.all()
#     return render(request, 'index.html', {'blogs': blogs})
#
# def traffic_laws(request):
#     traffic_laws = models.Traffic_Law.objects.all()
#     return render(request, 'index.html', {'traffic_laws': traffic_laws})