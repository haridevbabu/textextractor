# Generated by Django 3.1.1 on 2020-09-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_url', models.CharField(max_length=200)),
                ('extracted_text', models.TextField()),
            ],
        ),
    ]
