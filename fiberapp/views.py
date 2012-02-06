from django.http import HttpResponse
from django.shortcuts import render_to_response
from fiberapp.models import Source, Services, Farming, Garments
from fiberapp.models import Sheep_Breeds, Alpaca_Breeds, Rabbit_Breeds, Goat_Breeds, Plants
from django.views.generic.base import TemplateView
from django.template.defaultfilters import slugify
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

class JunkView(TemplateView):
    template_name='junk.html'
    def get_context_data(self, **kwargs):
        if len(self.args) == 1:
            return {'services_list':services(),'junk':self.args[0]}
        return {'services_list':services()}

class FarmingView(TemplateView):
    template_name = 'farming.html'
    tables = {'wool':'Sheep_Breeds',
                'alpaca':'Alpaca_Breeds',
                'rabbit':'Rabbit_Breeds',
                'goat':'Goat_Breeds',
                'plants':'Plants'}
    def get_context_data(self, **kwargs):
        artisans = Source.objects.filter(services__farming__isnull=False)
        # make a filter list for sidebar
        sidebar = []
        for field in Farming._meta.many_to_many:
            sidebar.append(field)
        second_level=""
        if len(self.args) == 1:
            keyword = "services__farming__"+slugify(self.args[0])+"__isnull"
            artisans = Source.objects.filter(**{keyword:False})
            sidebar = []
            for breed in eval('%s._meta.fields' % self.tables[self.args[0]]):
                if not breed.name is 'id':
                    sidebar.append(breed)
            second_level=slugify(self.args[0])
        elif len(self.args) == 2:
            keyword = "services__farming__"+slugify(self.args[0])+"__"+slugify(self.args[1])
            artisans = Source.objects.filter(**{keyword:True})

        return {'sidebar_list':sidebar,'services_list':services(),'artisan_list':artisans,'second_level':second_level}

class FabricView(TemplateView):
    template_name = 'fabric.html'
    def get_context_data(self, **kwargs):
        garments = []
        for field in Garments._meta.fields:
            if not field.name is 'id':
                garments.append(field)
        keyword = 'services__'+slugify(self.args[0])+"__isnull"
        artisans = Source.objects.filter(**{keyword:False})
        return {'sidebar_list':garments,'services_list':services(),'artisan_list':artisans,'fabric_type':slugify(self.args[0])}

class BasicView(TemplateView):
    template_name = 'basic.html'
    def get_context_data(self, **kwargs):
        if self.args[0] == "all":
            return {'artisan_list':Source.objects.all(),'services_list':services()}
        else: 
            keyword = 'services__'+slugify(self.args[0])
            artisans = Source.objects.filter(**{keyword:True})
            return {'artisan_list':artisans,'services_list':services()}
