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

def instructor_extended_info(request, id):
    instructor = models.Instructor.objects.get(id=id)
    return render(request, 'instructor_extended_info', {'instructor': instructor})

def course_extended_info(request, id):
    course = models.Course.objects.get(id=id)
    return render(request, 'course_extended_info', {'course': course})

def blogs_extended_info(request, id):
    blogs = models.Blog.objects.get(id=id)
    return render(request, 'blogs_extended_info', {'blogs': blogs})

def traffic_laws_extended_info(request, id):
    traffic_laws = models.Traffic_Law.objects.get(id=id)
    return render(request, 'traffic_laws_extended_info', {'traffic_laws': traffic_laws})
