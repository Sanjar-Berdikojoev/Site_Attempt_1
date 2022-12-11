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

class Frequently_Asked_QuestionsForm(forms.ModelForm):
    class Meta:
        model = models.Frequently_Asked_Questions
        fields = '__all__'

class AdvantagesForm(forms.ModelForm):
    class Meta:
        model = models.Advantages
        fields = '__all__'