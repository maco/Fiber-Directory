from django.http import HttpResponse
from django.shortcuts import render_to_response
from fiberapp.models import Services
from fiberapp.models import Materials
# Create your views here.

def master(request):
    print "hello world"
    services = []
    for field in Services._meta.fields:
        if not field.name is 'id':
            services.append(field)
    for field in Services._meta.many_to_many:
        services.append(field)
    for thing in services:
        print services.name
    return render_to_response('master.html',{'services_list':services})

def home(request):
    return render_to_response('index.html',{})

def materials(request):
    materials = []
    for field in Materials._meta.many_to_many:
        materials.append(field)

    return render_to_response('materials.html',{'materials_list':materials})
