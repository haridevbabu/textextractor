from rest_framework import serializers
from textextract.models import ExtractText

class ExtractTextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtractText
        fields =['id','blog_url','extracted_text',]


