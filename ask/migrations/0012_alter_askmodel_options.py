# Generated by Django 5.0 on 2024-04-04 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0011_alter_adminaskratingmodel_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='askmodel',
            options={'verbose_name': 'Ask', 'verbose_name_plural': 'Asks'},
        ),
    ]
