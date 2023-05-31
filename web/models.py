from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField
from django.core.validators import MinLengthValidator

# from django import forms
# from .models import Contact, Career, OurOffices
# from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


# Create your models here.







class Service(models.Model):
    image = VersatileImageField(upload_to = "service")
    name = models.CharField(max_length=100,blank=True,null=True,verbose_name="Service name")
    massage = models.CharField(max_length=70,verbose_name="Service page content")
    massage_1 = models.CharField(max_length=150, null=True,verbose_name="Service more page content")
    massage_2 = models.CharField(max_length=70, null=True,verbose_name="Service more headline")
    feature1 = models.CharField(max_length=200, null=True,verbose_name="Service feature 1")
    feature2 = models.CharField(max_length=200, null=True,verbose_name="Service feature 2")
    feature3 = models.CharField(max_length=200, null=True,verbose_name="Service feature 3")
    feature4 = models.CharField(max_length=200, null=True,verbose_name="Service feature 4")
    feature5 = models.CharField(max_length=200, null=True,verbose_name="Service feature 5")


    def __str__(self):
        return self.name
    


class CareerApply(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    qualification = models.CharField(max_length=100)
    career = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    


class ContactNumber(models.Model):
    number = models.IntegerField(null=True,blank=True)
    footernumber = models.IntegerField(null=True,blank=True)



class Career(models.Model):
    image = VersatileImageField(upload_to="Career")
    career = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Career title")
    Introduction = models.CharField(max_length=500, null=True, verbose_name="Career Introduction")
    points_headline_1 = models.CharField(max_length=100, null=True, verbose_name="points headline 1")
    detials_1_1 = HTMLField()
    points_headline_2 = models.CharField(max_length=100, null=True, verbose_name="points headline 2")
    detials_2_1 = HTMLField()
    points_headline_3 = models.CharField(max_length=100, null=True, verbose_name="points headline 3")
    detials_3_1 = HTMLField()
    
    def __str__(self):
        return self.career







class Project(models.Model):
    image = models.ImageField(upload_to = "HomeProject")
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class Banner(models.Model):
    caption=models.CharField(max_length=300)
    title=models.CharField(max_length=500)
    subtitle=models.CharField(max_length=700)
    image = VersatileImageField(upload_to = "home-banner") 
    
    def __str__(self):
        return self.caption


class MobileBanner(models.Model):
    caption=models.CharField(max_length=300)
    title=models.CharField(max_length=500)
    subtitle=models.CharField(max_length=700)
    image = VersatileImageField(upload_to = "mobile-banner") 
    
    def __str__(self):
        return self.caption




class Home_aboutimg(models.Model):
    image = VersatileImageField(upload_to = "home-svc-baner", blank=True,null=True)




class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to = "home-svc-baner")

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = VersatileImageField(upload_to = "home-banner") 
    career=models.CharField(max_length=500)
    stories=models.TextField(max_length=700)
    
    def __str__(self):
        return self.name
    



class Blog(models.Model):
    image = VersatileImageField(upload_to = "Blog image",verbose_name="Blog image")
    detials_1 = models.CharField(max_length=70,blank=True,null=True,verbose_name="Blog headline")
    detials_2 = models.CharField(max_length=70,blank=True,null=True,verbose_name="Blog content")
    detials_3 = models.CharField(max_length=400,blank=True,null=True,verbose_name="Blog content")
    detials_4 = models.CharField(max_length=200,blank=True,null=True,verbose_name="Blog content")


    class Meta:
        verbose_name = "Add Blog"
        verbose_name_plural = "Add Blogs"





class ServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name