# Generated by Django 5.0 on 2024-01-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0004_alter_askmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askmodel',
            name='content',
            field=models.TextField(default=None, null=True),
        ),
    ]