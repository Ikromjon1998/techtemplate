from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class MainIndexView(TemplateView):
    template_name = 'main/index.html'

class MainAboutView(TemplateView):
    template_name = 'main/about.html'

class MainContactView(TemplateView):
    template_name = 'main/contact.html'
