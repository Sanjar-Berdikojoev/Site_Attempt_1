from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Instructor(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField()
    extended_description = models.TextField(null=True)
    work_experience = models.PositiveSmallIntegerField(null=True)
    favorite_auto = models.CharField(max_length=100, null=True)

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

    def __str__(self):
        return self.title

class Blog(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    extended_description = models.TextField()

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
    post = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(User, max_length=100)
    rating_choices = RATING_CHOICES
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = []

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


