# Generated by Django 5.0 on 2024-02-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_askmodel_rating_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='askmodel',
            name='pinned',
            field=models.BooleanField(default=0),
        ),
    ]
