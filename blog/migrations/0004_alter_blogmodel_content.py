# Generated by Django 5.0 on 2024-01-08 04:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
