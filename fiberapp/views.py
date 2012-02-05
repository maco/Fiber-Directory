from django.http import HttpResponse
from django.shortcuts import render_to_response
from fiberapp.models import Services
from fiberapp.models import Farming
from fiberapp.models import Source
from django.views.generic.base import TemplateView
# Create your views here.


def services():
    services = []
    for field in Services._meta.fields:
        if not field.name is 'id':
            services.append(field)
    for field in Services._meta.many_to_many:
        services.append(field)
    return services

class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        return {'services_list':services()}

class FarmingView(TemplateView):
    template_name = 'farming.html'
    def get_context_data(self, **kwargs):
        farming = []
        for field in Farming._meta.many_to_many:
            print field.name
            farming.append(field)

        farmers = []

        return {'farming_list':farming,'services_list':services(),'farmer_list':farmers}

class BasicView(TemplateView):
    template_name = 'basic.html'
    def get_context_data(self, **kwargs):
        keyword = 'services__'+self.args[0]
        artisans = Source.objects.filter(**{keyword:1})
        return {'artisan_list':artisans,'services_list':services()}
