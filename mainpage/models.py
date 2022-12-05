from django.db import models

# Create your models here.
class Instructor(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField()

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