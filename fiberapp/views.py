from django.http import HttpResponse
from django.shortcuts import render_to_response
from fiberapp.models import Source, Services, Farming, Garments
from fiberapp.models import Sheep_Breeds, Alpaca_Breeds, Rabbit_Breeds, Goat_Breeds
from fiberapp.models import Dye_Plant_Breeds, Fiber_Plant_Breeds
from django.views.generic.base import TemplateView
from django.template.defaultfilters import slugify
from django.template.defaultfilters import title
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
    def get_context_data(self, **kwargs):
        artisans = Source.objects.filter(services__farming__isnull=False)
        second_level=""
        second_level_verbose=""
        third_level=""
        # make a filter list for sidebar
        sidebar = []
        type_list = {}
        for field in Farming._meta.many_to_many:
            keyword = field.name
            if Farming.objects.filter(**{keyword:True}):
                print field.name+" full"
                type_list[field] = "full"
            else:
                print field.name+" empty"
                type_list[field] = "empty"


        if len(self.args) == 1:
            keyword = "services__farming__"+slugify(self.args[0])+"__isnull"
            artisans = Source.objects.filter(**{keyword:False})
        elif len(self.args) == 2:
            keyword = "services__farming__"+slugify(self.args[0])+"__"+slugify(self.args[1])
            artisans = Source.objects.filter(**{keyword:True})
            for field in eval('%s_Breeds._meta.fields' % title(self.args[0])):
                if field.name == slugify(self.args[1]):
                    third_level = field.verbose_name

        if len(self.args) > 0:
            second_level=slugify(self.args[0])
            breed_list = {}
            # make a dictionary of breeds and whether they have data
            for breed in eval('%s_Breeds._meta.fields' % title(self.args[0])):
                if not breed.name is 'id':
                    keyword = breed.name
                    if eval('%s_Breeds' % title(self.args[0])).objects.filter(**{keyword:True}):
                        breed_list[breed] = "full"
                    else:
                        breed_list[breed] = "empty"
                        

            # Store verbose name for the category we're in
            for cat in Farming._meta.many_to_many:
                if cat.name == slugify(self.args[0]):
                    print cat.verbose_name
                    second_level_verbose = cat.verbose_name
            sidebar = [type_list, breed_list ]
        else:
            sidebar = type_list
        return {'sidebar_list':sidebar,'services_list':services(),'artisan_list':artisans,'second_level':second_level,'second_level_verbose':second_level_verbose,'third_level':third_level}

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
        if len(self.args) == 0 or self.args[0] == "all":
            return {'artisan_list':Source.objects.all(),'services_list':services()}
        else: 
            keyword = 'services__'+slugify(self.args[0])
            artisans = Source.objects.filter(**{keyword:True})
            return {'artisan_list':artisans,'services_list':services(),'slug':slugify(self.args[0])}
