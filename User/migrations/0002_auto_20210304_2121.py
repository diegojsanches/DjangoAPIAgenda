# Generated by Django 3.1.7 on 2021-03-04 21:21

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to=User.models.pathUploadProfilePhoto),
        ),
    ]
