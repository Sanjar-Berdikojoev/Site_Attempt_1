# Generated by Django 4.1.3 on 2022-12-14 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_customuser_gender_alter_customuser_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
