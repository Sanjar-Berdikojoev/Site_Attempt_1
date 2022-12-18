from django import forms
from . import models
from django.forms import TextInput, Textarea, Select

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body', 'rating']
        widgets = {
            'body': Textarea(attrs= {
                'class': 'reviews__form-field',
                'placeholder': 'Write a comment',
                'name': 'review',
                'id': '',
                'cols': '30',
                'rows': '10',
            }),
            'rating': Select(attrs={
                'class': 'reviews__form-select',
                'name': 'select',
            })
        }

class Aplly_For_JobForm(forms.ModelForm):

    class Meta:
        model = models.Aplly_For_Job
        fields = ['name', 'surname', 'phone_number', 'email']
        widgets = {
            'name': TextInput(attrs= {
                'type': 'text',
                'placeholder': 'Your name',
            }),
            'surname': TextInput(attrs= {
                'type': 'text',
                'placeholder': 'Your surname',
            }),
            'phone_number': TextInput(attrs= {
                'type': 'number',
                'placeholder': 'Your phone number',
            }),
            'email': TextInput(attrs= {
                'type': 'email',
                'placeholder': 'Your email',
            }),
        }


class Aplly_For_CourseForm(forms.ModelForm):

    class Meta:
        model = models.Aplly_For_Course
        fields = ['name', 'surname', 'phone_number', 'age', 'email', 'category_choice']
        widgets = {
            'name': TextInput(attrs= {
                'type': 'text',
                'placeholder': 'Your name',
            }),
            'surname': TextInput(attrs= {
                'type': 'text',
                'placeholder': 'Your surname',
            }),
            'phone_number': TextInput(attrs= {
                'type': 'number',
                'placeholder': 'Your phone number',
            }),
            'age': TextInput(attrs= {
                'type': 'number',
                'placeholder': 'Your age',
            }),
            'email': TextInput(attrs={
                'type': 'email',
                'placeholder': 'Your email',
            }),
            'category_choice': Select(attrs={
                'type': 'text',
                'placeholder': 'Choose category',
            }),
        }