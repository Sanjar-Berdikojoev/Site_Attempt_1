# Generated by Django 4.1.3 on 2022-12-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_alter_instructor_review_rating_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor_review',
            name='post',
        ),
        migrations.AddField(
            model_name='instructor_review',
            name='post',
            field=models.ManyToManyField(blank=True, to='mainpage.instructor'),
        ),
    ]
