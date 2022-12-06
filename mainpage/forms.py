from django import forms
from . import models
class InstructorForm(forms.ModelForm):
    class Meta:
        model = models.Instructor
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = '__all__'

class Traffic_LawForm(forms.ModelForm):
    class Meta:
        model = models.Traffic_Law
        fields = '__all__'