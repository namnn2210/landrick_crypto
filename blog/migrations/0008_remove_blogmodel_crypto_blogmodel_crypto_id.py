# Generated by Django 5.0 on 2024-04-06 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_cryptoblogmodel_blogcategorymodel_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='crypto',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='crypto_id',
            field=models.IntegerField(null=True),
        ),
    ]