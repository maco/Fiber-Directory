from fiberapp.models import Sheep_Breeds
from fiberapp.models import Rabbit_Breeds
from fiberapp.models import Alpaca_Breeds
from fiberapp.models import Goat_Breeds
from fiberapp.models import Plants
from fiberapp.models import Garments
from fiberapp.models import Services
from fiberapp.models import Source

from django.contrib import admin

class Sheep_Breeds_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Finewool', {'fields':[
            'cvm',
            'cormo',
            'merino',
            'polwarth',
            'rambouillet',
            'romeldale',
            'targhee']}),
        ('Mediumwool',{'fields':[
            'california_red',
            'columbia',
            'corriedale',
            'finnish_landrace',
            'montadale',
            'tunis']}),
        ('Down and Down-Type Wool',{'fields':[
            'cheviot',
            'clun_forest',
            'dorset_down',
            'dorset_horn',
            'oxford',
            'ryeland',
            'shropshire',
            'southdown',
            'suffolk']}),
        ('Longwool',{'fields':[
            'bluefaced_leicester',
            'border_leicester',
            'coopworth',
            'cotswold',
            'leicester_longwool',
            'lincoln',
            'perendale',
            'romney',
            'teeswater',
            'wensleydale']}),
        ('Dual-coated and Primitive',{'fields':[
            'icelandic',
            'jacob',
            'navajo_churro',
            'scottish_blackface',
            'shetland']})
    ]

admin.site.register(Sheep_Breeds,Sheep_Breeds_Admin)
admin.site.register(Rabbit_Breeds)
admin.site.register(Alpaca_Breeds)
admin.site.register(Goat_Breeds)
admin.site.register(Plants)
admin.site.register(Garments)
admin.site.register(Services)
admin.site.register(Source)
