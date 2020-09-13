from django.db import models

# Create your models here.


class ExtractText(models.Model):
    blog_url = models.URLField(max_length=300)
    extracted_text = models.TextField()
