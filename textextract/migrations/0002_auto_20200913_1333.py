# Generated by Django 3.1.1 on 2020-09-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textextract', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracttext',
            name='blog_url',
            field=models.URLField(),
        ),
    ]