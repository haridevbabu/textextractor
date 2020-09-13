from django.shortcuts import render
import requests
import html2text
from textextract.forms import UrlForm
from django.http import HttpResponse,JsonResponse
from textextract.models import ExtractText
from django.views.generic import TemplateView,FormView,CreateView,UpdateView
# Create your views here.
from rest_framework import viewsets
from django.urls import reverse

# import local data
from .serializers import ExtractTextSerializer

from django import forms


def gettext(request):
    if request.method == 'POST':
        obj = ExtractText()
        form = UrlForm(request.POST)


        if form.is_valid():

            blog_url = form.cleaned_data['blog_url']
            response1 = requests.get(blog_url)
            if response1.status_code == 200:
                content = response1.text
                extracted_text1 = html2text.html2text(content)
                obj.extracted_text = extracted_text1
                obj.blog_url = blog_url
                form.save()
                obj.save()
            form = UrlForm()  # display empty form
            context = {'form': form}
            template = "extract.html"
            return render(request, template, context)
            return render(request,'extract.html')
        else:
            return HttpResponse("invalid form")






    else:
        form = UrlForm()  # display empty form
        context = {'form': form}
        template = "extract.html"
        return render(request, template, context)





class ExtractTextView(viewsets.ModelViewSet):
    # define queryset
    queryset = ExtractText.objects.all()

    # specify serializer to be used
    serializer_class = ExtractTextSerializer




