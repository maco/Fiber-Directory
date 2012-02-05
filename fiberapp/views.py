from django.http import HttpResponse
from django.shortcuts import render_to_response
from fiberapp.models import Services
from fiberapp.models import Farming
from fiberapp.models import Source
from fiberapp.models import Garments
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
        return {'farming_list':farming,'services_list':services(),'artisan_list':Source.objects.filter(services__farming=1)}

class FabricView(TemplateView):
    template_name = 'fabric.html'
    def get_context_data(self, **kwargs):
        garments = []
        for field in Garments._meta.fields:
            if not field.name is 'id':
                garments.append(field)
        keyword = 'services__'+self.args[0]
        artisans = Source.objects.filter(**{keyword:1})
        return {'garment_list':garments,'services_list':services(),'artisan_list':artisans,'fabric_type':self.args[0]}

class BasicView(TemplateView):
    template_name = 'basic.html'
    def get_context_data(self, **kwargs):
        if self.args[0] == "all":
            return {'artisan_list':Source.objects.all(),'services_list':services()}
        else: 
            keyword = 'services__'+self.args[0]
            artisans = Source.objects.filter(**{keyword:1})
            return {'artisan_list':artisans,'services_list':services()}
