# Generated by Django 2.2.1 on 2020-05-06 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0002_introduction_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='introduction',
            options={'ordering': ['category']},
        ),
    ]
