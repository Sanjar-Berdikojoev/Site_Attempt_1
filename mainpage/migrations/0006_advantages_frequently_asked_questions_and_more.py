# Generated by Django 4.1.3 on 2022-12-12 03:33

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_instructor_extended_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Frequently_Asked_Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='favorite_auto',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='work_experience',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Instructor_Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=django.contrib.auth.models.User)),
                ('comment', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mainpage.instructor')),
            ],
            options={
                'ordering': [],
            },
        ),
    ]
