from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.views import generic
import numpy as np
from .forms import CommentForm, Apply_For_JobForm, Apply_For_CourseForm

def error_404(request, exception):
    return render(request, '404.html')

def mainpage_all(request):
    instructor = models.Instructor.objects.order_by('id')[:5]
    course = models.Course.objects.order_by('id')[:2]
    blogs = models.Blog.objects.order_by('id')[:3]
    traffic_laws = models.Traffic_Law.objects.order_by('id')[:4]
    advantages = models.Advantages.objects.order_by('id')[:3]
    frequently_asked_questions = models.Frequently_Asked_Questions.objects.order_by('id')[:5]
    context = {
        'instructor': instructor,
        'course': course,
        'blogs': blogs,
        'traffic_laws': traffic_laws,
        'advantages': advantages,
        'frequently_asked_questions': frequently_asked_questions
    }
    return render(request, 'index.html', context)

def application_success(request):
    return render(request, 'success.html')

class InstructorCreateView(generic.CreateView):
    template_name = 'models_create.html'
    form_class = forms.InstructorForm
    queryset = models.Instructor.objects.all()
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(InstructorCreateView, self).form_valid(form=form)


class InstructorUpdateView(generic.UpdateView):
    template_name = 'models_update.html'
    form_class = forms.InstructorForm
    success_url = 'http://127.0.0.1:8000'


    def get_object(self, **kwargs):
        course_id = self.kwargs.get('id')
        return get_object_or_404(models.Instructor, id=course_id)


class InstructorDeleteView(generic.DeleteView):
    template_name = 'models_delete.html'
    form_class = forms.InstructorForm
    queryset = models.Instructor.objects.all()
    success_url = 'http://127.0.0.1:8000'
    slug_field = 'product_slug'
    slug_url_kwarg = 'product_slug'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(InstructorDeleteView, self).form_valid(form=form)


class BlogCreateView(generic.CreateView):
    template_name = 'models_create.html'
    form_class = forms.BlogForm
    queryset = models.Blog.objects.all()
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BlogCreateView, self).form_valid(form=form)


class BlogUpdateView(generic.UpdateView):
    template_name = 'models_update.html'
    form_class = forms.BlogForm
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(models.Blog, id=blog_id)

    def form_valid(self, form):
        return super(BlogUpdateView, self).form_valid(form=form)


class BlogDeleteView(generic.DeleteView):
    template_name = 'models_delete.html'
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(models.Blog, id=blog_id)


class CommentView(generic.ListView):
    template_name = 'instructors_info.html'
    queryset = models.Comment.objects.all()

    def get_queryset(self):
        return models.Comment.objects.all()


class FAQView(generic.ListView):
    template_name = 'faqs.html'
    queryset = models.Frequently_Asked_Questions.objects.all()

    def get_queryset(self):
        return models.Frequently_Asked_Questions.objects.all()


class CoursesView(generic.ListView):
    template_name = 'courses.html'
    queryset = models.Course.objects.all()

    def get_queryset(self):
        return models.Course.objects.all()


def instructor_view(request):
    if request.method == 'POST':
        form = Apply_For_JobForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('application_success/')

    instructor = models.Instructor.objects.all()
    job_applying_form = Apply_For_JobForm()
    context = {
        'instructor': instructor,
        'job_applying_form': job_applying_form,
    }

    return render(request, 'instructors.html', context)


def contacts_view(request):
    if request.method == 'POST':
        form = Apply_For_JobForm(request.POST)
        if form.is_valid():
            form.save()

    job_applying_form = Apply_For_JobForm()
    return render(request, 'contacts.html', {'job_applying_form': job_applying_form,})

def instructor_detail(request, id):
    instructor = models.Instructor.objects.get(id=id)
    return render(request, 'instructors_info.html', {'instructor': instructor})

class InstructorDetailView(generic.DetailView):
    template_name = 'instructors_info.html'

    def get_object(self, **kwargs):
        instructor_id = self.kwargs.get('id')
        return get_object_or_404(models.Instructor, id=instructor_id)

def about_us_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('application_success/')

    comment = models.Comment.objects.all()
    comment_form = CommentForm()
    context = {
        'comment': comment,
        'comment_form': comment_form,
    }
    return render(request, 'about_us.html', context)


def course_detail(request, id):
    if request.method == 'POST':
        form = Apply_For_CourseForm(request.POST)
        if form.is_valid():
            form.save()

    course = models.Course.objects.get(id=id)
    course_applying_form = Apply_For_CourseForm()
    context = {
        'course': course,
        'course_applying_form': course_applying_form,
    }
    return render(request, 'courses_info.html', context)


class BlogsView(generic.ListView):
    template_name = 'blog.html'
    queryset = models.Blog.objects.all()

    def get_queryset(self):
        return models.Blog.objects.all()

class BlogsDetailView(generic.DetailView):
    template_name = 'blog_info.html'

    def get_object(self, **kwargs):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(models.Blog, id=blog_id)


def traffic_rules_view(request):
    traffic_rule = models.Traffic_Rule.objects.all()
    warning_sign = models.Warning_Signs.objects.all()
    priority_sign = models.Priotity_Signs.objects.all()
    prohibition_sign = models.Prohibition_Signs.objects.all()
    mandatory_sign = models.Mandatory_Signs.objects.all()
    sign_of_special_regulations = models.Signs_Of_Special_Regulations.objects.all()
    information_sign = models.Information_Signs.objects.all()
    service_mark = models.Service_Marks.objects.all()
    sign_of_additional_information = models.Signs_Of_Additional_Information.objects.all()
    context = {
            'traffic_rule': traffic_rule,
            'warning_sign': warning_sign,
            'priority_sign': priority_sign,
            'prohibition_sign': prohibition_sign,
            'mandatory_sign': mandatory_sign,
            'sign_of_special_regulations': sign_of_special_regulations,
            'information_sign': information_sign,
            'service_mark': service_mark,
            'sign_of_additional_information': sign_of_additional_information,
    }
    return render(request, 'traffic_laws.html', context)

class Traffic_RulesDetailView(generic.DetailView):
    template_name = 'traffic_laws_info.html'

    def get_object(self, **kwargs):
        traffic_rule_id = self.kwargs.get('id')
        return get_object_or_404(models.Traffic_Rule, id=traffic_rule_id)



