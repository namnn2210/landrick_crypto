# Generated by Django 5.0 on 2023-12-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0002_askmodel_content_alter_askmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='askmodel',
            name='slug',
            field=models.TextField(default='slug'),
        ),
    ]
