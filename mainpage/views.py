from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic
import numpy as np

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

def admin_panel_all(request):
    instructor = models.Instructor.objects.all()
    course = models.Course.objects.all()
    blogs = models.Blog.objects.all()
    traffic_laws = models.Traffic_Law.objects.all()
    advantages = models.Advantages.objects.all()
    frequently_asked_questions = models.Frequently_Asked_Questions.objects.all()
    context = {
        'instructor':instructor,
        'course': course,
        'blogs': blogs,
        'traffic_laws': traffic_laws,
        'advantages': advantages,
        'frequently_asked_questions': frequently_asked_questions,
    }
    return render(request, 'admin_panel.html', context)

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
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        instructor_id = self.kwargs.get('id')
        return get_object_or_404(models.Instructor, id=instructor_id)

    def form_valid(self, form):
        return super(InstructorUpdateView, self).form_valid(form=form)


class InstructorDeleteView(generic.DeleteView):
    template_name = 'models_delete.html'
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        instructor_id = self.kwargs.get('id')
        return get_object_or_404(models.Instructor, id=instructor_id)


class CourseCreateView(generic.CreateView):
    template_name = 'models_create.html'
    form_class = forms.CourseForm
    queryset = models.Course.objects.all()
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CourseCreateView, self).form_valid(form=form)


class CourseUpdateView(generic.UpdateView):
    template_name = 'models_update.html'
    form_class = forms.CourseForm
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        course_id = self.kwargs.get('id')
        return get_object_or_404(models.Course, id=course_id)

    def form_valid(self, form):
        return super(CourseUpdateView, self).form_valid(form=form)


class CourseDeleteView(generic.DeleteView):
    template_name = 'models_delete.html'
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        course_id = self.kwargs.get('id')
        return get_object_or_404(models.Course, id=course_id)


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


class Traffic_LawCreateView(generic.CreateView):
    template_name = 'models_create.html'
    form_class = forms.Traffic_LawForm
    queryset = models.Traffic_Law.objects.all()
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Traffic_LawCreateView, self).form_valid(form=form)


class Traffic_LawUpdateView(generic.UpdateView):
    template_name = 'models_update.html'
    form_class = forms.Traffic_LawForm
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        traffic_law_id = self.kwargs.get('id')
        return get_object_or_404(models.Traffic_Law, id=traffic_law_id)

    def form_valid(self, form):
        return super(Traffic_LawUpdateView, self).form_valid(form=form)


class Traffic_LawDeleteView(generic.DeleteView):
    template_name = 'models_delete.html'
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        traffic_law_id = self.kwargs.get('id')
        return get_object_or_404(models.Traffic_Law, id=traffic_law_id)


class Frequently_Asked_QuestionsCreateView(generic.CreateView):
    template_name = 'models_create.html'
    form_class = forms.Frequently_Asked_QuestionsForm
    queryset = models.Frequently_Asked_Questions.objects.all()
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Frequently_Asked_QuestionsCreateView, self).form_valid(form=form)


class Frequently_Asked_QuestionsUpdateView(generic.UpdateView):
    template_name = 'models_update.html'
    form_class = forms.Frequently_Asked_QuestionsForm
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        frequently_asked_questions_id = self.kwargs.get('id')
        return get_object_or_404(models.Frequently_Asked_Questions, id=frequently_asked_questions_id)

    def form_valid(self, form):
        return super(Frequently_Asked_QuestionsUpdateView, self).form_valid(form=form)


class Frequently_Asked_QuestionsDeleteView(generic.DeleteView):
    template_name = 'models_delete.html'
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        frequently_asked_questions_id = self.kwargs.get('id')
        return get_object_or_404(models.Frequently_Asked_Questions, id=frequently_asked_questions_id)


class AdvantagesCreateView(generic.CreateView):
    template_name = 'models_create.html'
    form_class = forms.AdvantagesForm
    queryset = models.Advantages.objects.all()
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AdvantagesCreateView, self).form_valid(form=form)


class AdvantagesUpdateView(generic.UpdateView):
    template_name = 'models_update.html'
    form_class = forms.AdvantagesForm
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        advantages_id = self.kwargs.get('id')
        return get_object_or_404(models.Advantages, id=advantages_id)

    def form_valid(self, form):
        return super(AdvantagesUpdateView, self).form_valid(form=form)


class AdvantagesDeleteView(generic.DeleteView):
    template_name = 'models_delete.html'
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        advantages_id = self.kwargs.get('id')
        return get_object_or_404(models.Advantages, id=advantages_id)


def instructor_reviews(request):
    reviews = models.Instructor_Review.objects.all()
    return render(request, 'instructors_extended_info', {'reviews': reviews})

def average_rating(self):
    all_ratings = list(map(lambda x: x.value, self.comments.all()))
    average = np.array(all_ratings).astype(np.float)
    return np.average(average)
