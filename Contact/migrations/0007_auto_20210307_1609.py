# Generated by Django 3.1.7 on 2021-03-07 16:09

import Contact.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0006_auto_20210306_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, upload_to=Contact.models.pathUploadContactImage),
        ),
    ]
