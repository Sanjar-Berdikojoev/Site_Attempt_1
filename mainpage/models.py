from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Instructor(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField()
    extended_description = models.TextField(null=True)
    general_experience = models.PositiveSmallIntegerField(null=True)
    teaching_experience = models.PositiveSmallIntegerField(null=True)
    teaching_category = models.CharField(max_length=3, null=True)
    driving_car = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    post = models.ManyToManyField('Instructor_Review', blank=True, related_name='post')


    def __str__(self):
        return self.title

class Course(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField()
    extended_description = models.TextField()
    price = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    lessons = models.PositiveIntegerField()
    age = models.PositiveSmallIntegerField(null=True)
    practice = models.PositiveIntegerField(null=True)
    category_letter = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    extended_description = models.TextField()
    extended_description_2 = models.TextField(null=True)
    user = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
class Traffic_Law(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField()
    extended_description = models.TextField()

    def __str__(self):
        return self.title

class Frequently_Asked_Questions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

class Advantages(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title


RATING_CHOICES = (
    ('5', 'Excellent'),
    ('4', 'Good'),
    ('3', 'Normal'),
    ('2', 'Bad'),
    ('1', 'Terrible'),
)


class Instructor_Review(models.Model):
    name = models.CharField(User, max_length=100)
    rating_choices = models.CharField(choices = RATING_CHOICES, null=True, max_length=25)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)




