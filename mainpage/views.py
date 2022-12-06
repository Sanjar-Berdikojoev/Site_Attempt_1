from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

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
    return render(request, 'instructor_extended_info.html', {'instructor': instructor})

def course_extended_info(request, id):
    course = models.Course.objects.get(id=id)
    return render(request, 'course_extended_info.html', {'course': course})

def blogs_extended_info(request, id):
    blogs = models.Blog.objects.get(id=id)
    return render(request, 'blogs_extended_info.html', {'blogs': blogs})

def traffic_laws_extended_info(request, id):
    traffic_laws = models.Traffic_Law.objects.get(id=id)
    return render(request, 'traffic_laws_extended_info.html', {'traffic_laws': traffic_laws})


class InstructorCreateView(generic.CreateView):
    template_name = 'instructor_create.html'
    form_class = forms.InstructorForm
    queryset = models.Instructor.objects.all()
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(InstructorCreateView, self).form_valid(form=form)


class InstructorUpdateView(generic.UpdateView):
    template_name = 'instructor_update.html'
    form_class = forms.InstructorForm
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        instructor_id = self.kwargs.get('id')
        return get_object_or_404(models.Instructor, id=instructor_id)

    def form_valid(self, form):
        return super(InstructorUpdateView, self).form_valid(form=form)


class InstructorDeleteView(generic.DeleteView):
    template_name = 'instructor_delete.html'
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        instructor_id = self.kwargs.get('id')
        return get_object_or_404(models.Instructor, id=instructor_id)
