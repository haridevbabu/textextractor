# Generated by Django 3.1.1 on 2020-09-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textextract', '0002_auto_20200913_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracttext',
            name='blog_url',
            field=models.URLField(max_length=300),
        ),
    ]