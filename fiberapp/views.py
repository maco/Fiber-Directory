from django.http import HttpResponse
from django.shortcuts import render_to_response
from fiberapp.models import Services
from fiberapp.models import Materials
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

class MaterialsView(TemplateView):
    template_name = 'materials.html'
    def get_context_data(self, **kwargs):
        materials = []
        for field in Materials._meta.many_to_many:
            print field.name
            materials.append(field)

        return {'materials_list':materials,'services_list':services()}
