from django.contrib import admin
from django import forms
from django.db import models
from . forms import CareerForm
from . forms import ContactNumberAdminForm
from versatileimagefield.fields import VersatileImageField




from . models import Service
from . models import CareerApply
from . models import ServiceRequest
from . models import Career
from . models import Contact
from . models import Project
from . models import Banner
from . models import MobileBanner
from . models import Brand
from . models import Home_aboutimg
from . models import Client
from . models import Blog
from . models import ContactNumber


# how to diffrent type admin.?

admin.site.register(CareerApply)
admin.site.register(ServiceRequest)
admin.site.register(Contact)
admin.site.register(Project)




@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    form = CareerForm
    fieldsets = [
        ('Career page Information', {'fields': ['image', 'career', 'title', 'Introduction',]}),
        ('Career apply page headline 1', {'fields': ['points_headline_1', 'detials_1_1' ]}),
        ('Career apply page headline 2', {'fields': ['points_headline_2', 'detials_2_1' ]}),
        ('Career apply page headline 3', {'fields': ['points_headline_3', 'detials_3_1' ]}),
    ]
    

admin.site.register(Banner)
admin.site.register(MobileBanner)
admin.site.register(Brand)
admin.site.register(Home_aboutimg)
admin.site.register(Client)
admin.site.register(Blog)



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Service page Information', {'fields': ['image', 'name', 'massage',]}),
        ('Service more page content maximum 150 Characters', {'fields': [ 'massage_1']}),
        ('Service more page headline maximum 70 Characters', {'fields': [ 'massage_2']}),
        ('Service more page features maximum 200 Characters', {'fields': [ 'feature1', 'feature2', 'feature3', 'feature4', 'feature5']}),
    ]


class ContactNumberAdmin(admin.ModelAdmin):
    form = ContactNumberAdminForm


# admin.site.register(ContactNumber)
admin.site.register(ContactNumber, ContactNumberAdmin)
