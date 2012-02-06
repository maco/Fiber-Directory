from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField
import string

# Create your models here.
class Sheep_Breeds(models.Model):
    merino = models.BooleanField(default=False)
    cormo = models.BooleanField(default=False)
    wensleydale = models.BooleanField(default=False)
    corriedale = models.BooleanField(default=False)
    leicester_longwool = models.BooleanField(default=False)
    bluefaced_leicester = models.BooleanField(default=False)
    cvm = models.BooleanField("CVM",default=False)
    polwarth = models.BooleanField(default=False)
    rambouillet = models.BooleanField(default=False)
    romeldale = models.BooleanField(default=False)
    targhee = models.BooleanField(default=False)
    california_red = models.BooleanField(default=False)
    columbia = models.BooleanField(default=False)
    finnish_landrace = models.BooleanField(default=False)
    montadale = models.BooleanField(default=False)
    tunis = models.BooleanField(default=False)
    cheviot = models.BooleanField(default=False)
    clun_forest = models.BooleanField(default=False)
    dorset_down = models.BooleanField(default=False)
    dorset_horn = models.BooleanField("dorset horn or poll dorset",default=False)
    oxford = models.BooleanField(default=False)
    ryeland = models.BooleanField(default=False)
    shropshire = models.BooleanField(default=False)
    southdown = models.BooleanField(default=False)
    suffolk = models.BooleanField(default=False)
    border_leicester = models.BooleanField(default=False)
    coopworth = models.BooleanField(default=False)
    cotswold = models.BooleanField(default=False)
    lincoln = models.BooleanField(default=False)
    perendale = models.BooleanField(default=False)
    romney = models.BooleanField(default=False)
    teeswater = models.BooleanField(default=False)
    icelandic = models.BooleanField(default=False)
    jacob = models.BooleanField(default=False)
    navajo_churro = models.BooleanField("navajo-churro",default=False)
    scottish_blackface = models.BooleanField(default=False)
    shetland = models.BooleanField(default=False)
    
class Rabbit_Breeds(models.Model):
    french_angora = models.BooleanField(default=False)
    german_angora = models.BooleanField(default=False)
    english_angora = models.BooleanField(default=False)

class Alpaca_Breeds(models.Model):
    suri = models.BooleanField(default=False)
    huayaca = models.BooleanField(default=False)

class Goat_Breeds(models.Model):
    kashmir = models.BooleanField("kashmir (cashmere)",default=False)
    angora = models.BooleanField("angora (mohair)",default=False)

class Plants(models.Model):
    TYPE_CHOICES = (
        (u'fiber',u'Fiber'),
        (u'dye',u'Dye')
    )
    name = models.CharField(max_length=64,primary_key=True)
    plant_type = models.CharField(max_length=20,choices=TYPE_CHOICES)

class Garments(models.Model):
    hats = models.BooleanField(default=False)
    scarves = models.BooleanField(default=False)
    socks = models.BooleanField(default=False)
    shawls = models.BooleanField(default=False)
    sweaters = models.BooleanField(default=False)
    shirts = models.BooleanField(default=False)
    skirts = models.BooleanField(default=False)
    trousers = models.BooleanField(default=False)
    dresses = models.BooleanField(default=False)
    hands = models.BooleanField("mittens and gloves",default=False)
    def __unicode__(self):
        garments = []
        if self.hats == True:
            garments.append("hats")
        if self.scarves == True:
            garments.append("scarves")
        if self.socks == True:
            garments.append("socks")
        if self.shawls == True:
            garments.append("shawls")
        if self.sweaters == True:
            garments.append("sweaters")
        if self.shirts == True:
            garments.append("shirts")
        if self.skirts == True:
            garments.append("skirts")
        if self.trousers == True:
            garments.append("trousers")
        if self.dresses == True:
            garments.append("dresses")
        if self.hands == True:
            garments.append("gloves/mittens")
        mystr = string.join(garments,", ")
        return mystr

class Farming(models.Model):
    sheep = models.ManyToManyField(Sheep_Breeds,blank=True)
    rabbit = models.ManyToManyField(Rabbit_Breeds,blank=True)
    goat = models.ManyToManyField(Goat_Breeds,blank=True)
    alpaca  = models.ManyToManyField(Alpaca_Breeds,blank=True)
    plant = models.ManyToManyField(Plants,blank=True,verbose_name="plants")

class Services(models.Model):
    farming = models.ManyToManyField(Farming,blank=True,verbose_name="farming")
    raw_fiber = models.BooleanField(default=False)
    roving = models.BooleanField(default=False)
    fleece_prep = models.BooleanField(default=False)
    handspinning = models.BooleanField(default=False)
    millspinning = models.BooleanField(default=False)
    weaving = models.BooleanField(default=False)
    knitting = models.ManyToManyField(Garments,related_name="%(app_label)s_%(class)s_related_knitting",blank=True)
    crochet = models.ManyToManyField(Garments,related_name="%(app_label)s_%(class)s_related_crochet",blank=True)
    sewing = models.ManyToManyField(Garments,related_name="%(app_label)s_%(class)s_related_sewing",blank=True)
    dyeing = models.BooleanField(default=False)
    felting = models.BooleanField(default=False)

    def __unicode__(self):
        services = []
        if self.farming.count() > 0:
            services.append("farming")
        if self.raw_fiber == True:
            services.append("raw fiber")
        if self.roving == True:
            services.append("roving")
        if self.fleece_prep == True:
            services.append("fleece preparation")
        if self.handspinning == True:
            services.append("handspinning")
        if self.millspinning == True:
            services.append("millspinning")
        if self.weaving == True:
            services.append("weaving")
        if self.knitting.count() > 0:
            services.append("knitting")
        if self.crochet.count() > 0:
            services.append("crochet")
        if self.sewing.count() > 0:
            services.append("sewing")
        if self.dyeing == True:
            services.append("dyeing")
        if self.felting == True:
            services.append("felting")

        mystr = string.join(services,", ")
        return mystr

class Source(models.Model):
    STATE_CHOICES = (
        (u'DC',u'District of Columbia'),
        (u'DE',u'Delaware'),
        (u'MD',u'Maryland'),
        (u'PA',u'Pennsylvania'),
        (u'VA',u'Virginia')
    )
    name = models.CharField(max_length=100,primary_key=True,unique=True)
    contact_name = models.CharField(max_length=100,blank=True)
    street_address = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=2,choices=STATE_CHOICES,blank=True)
    zip_code = models.CharField(max_length=10,blank=True)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=254,blank=True)
    url = models.URLField(verify_exists=True,max_length=255,blank=True)
    services = models.ManyToManyField(Services,related_name="%(app_label)s_%(class)s_related")
    notes = models.CharField(max_length=500,blank=True)

    def __unicode__(self):
        mystr = self.name+"\n"+self.contact_name+"\n"+self.street_address+"\n"+self.city+", "+self.state+"  "+self.zip_code+"\n"+self.phone+"\n"+self.email+"\n"+self.url
        return mystr
