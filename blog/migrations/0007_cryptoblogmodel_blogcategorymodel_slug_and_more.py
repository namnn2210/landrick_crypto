# Generated by Django 5.0 on 2024-04-04 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogmodel_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoBlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('symbol', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='blogcategorymodel',
            name='slug',
            field=models.TextField(default='slug'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='crypto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.cryptoblogmodel'),
        ),
    ]