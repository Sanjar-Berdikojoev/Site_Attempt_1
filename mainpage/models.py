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
    teaching_category = models.CharField(max_length=10, null=True)
    driving_car = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)


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
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Normal', 'Normal'),
    ('Bad', 'Bad'),
    ('Awful', 'Awful'),
)


class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    rating = models.CharField(choices=RATING_CHOICES, max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)


class Aplly_For_Job(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)


CATEGORY_CHOICES = (
    ('A', 'A'),
    ('A1', 'A1'),
    ('B', 'B'),
    ('B1', 'B1'),
    ('C', 'C'),
    ('C1', 'C1'),
    ('D', 'D'),
    ('E', 'E'),
)

class Aplly_For_Course(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=100)
    category_choice = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)


class Traffic_Rule(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField()


class Warning_Signs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()


class Priotity_Signs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()

class Prohibition_Signs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()

class Mandatory_Signs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()

class Signs_Of_Special_Regulations(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()


class Information_Signs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()


class Service_Marks(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()

class Signs_Of_Additional_Information(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
