from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


from web.models import Service
from web.models import Career
from web.models import CareerApply
from web.models import ServiceRequest
from web.models import Contact
from web.models import Project
from web.models import Banner
from web.models import MobileBanner
from web.models import Client
from web.models import Brand
from web.models import Blog
from web.models import ContactNumber

from web.models import Home_aboutimg



# from ..forms import ContactForm
# Create your views here.




def index(request):
    number=ContactNumber.objects.first()
    project = Project.objects.all()
    table = Service.objects.all()
    banner = Banner.objects.all()
    mobileBanner = MobileBanner.objects.all()
    brand = Brand.objects.all()
    client = Client.objects.all()
    blog=Blog.objects.all()
    home_aboutimg = Home_aboutimg.objects.first()
    context = {"project": project, "table": table, "banner":banner, "mobileBanner":mobileBanner,'brand': brand, "home_aboutimg":home_aboutimg,"client": client,"blog": blog,"number":number}
    
    return render(request, 'web/index.html', context)




def about(request):
    number=ContactNumber.objects.first()
    client = Client.objects.all()
    brand = Brand.objects.all()
    context={"client": client,"brand": brand,"number":number}
    return render(request,'web/about.html' ,context)


def services(request):
    number=ContactNumber.objects.first()
    table=Service.objects.all()
    context={"table":table,"number":number}
    return render(request,'web/services.html',context)




def single_service(request,id):
    number=ContactNumber.objects.first()
    table=Service.objects.get(id=id)
    context={"table":table,"number":number}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        location = request.POST.get('location')
        message = request.POST.get('message')

        services = ServiceRequest(name=name, email=email, phone=phone, message=message,service=service,location=location,)
        services.save()

        email_content = render_to_string('web/email_template.html', {
            'name': name,
            'phone': phone,
            'email': email,
            'service': service,
            'location': location,
            'message': message
        })
        # Send the email
        send_mail(
            'Nayel service request',
            '',
            settings.DEFAULT_FROM_EMAIL,
            ['kfaamardesubombhack@gmail.com'],
            html_message=email_content,
            fail_silently=False,
        )

        return render(request,'web/single-service.html',context)
    return render(request,'web/single-service.html',context)


def contact(request):
    number=ContactNumber.objects.first()
    context={"number":number}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message,)
        contact.save()
        
    return render(request,'web/contact.html',context)


def career(request):
    number=ContactNumber.objects.first()
    career=Career.objects.all()
    context={"career":career,"number":number}
    return render(request,'web/career.html',context)


def career_apply(request,id):
    number=ContactNumber.objects.first()
    career=Career.objects.get(id=id)
    context={"career":career,"number":number}
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        qualification = request.POST.get('qualification')
        career = request.POST.get('career')

        careers = CareerApply(name=name, email=email, phone=phone, message=message,qualification=qualification,career=career,)
        careers.save()
        return render(request,"web/career-apply.html",context)

        
    return render(request,"web/career-apply.html",context)




def blog(request):
    number=ContactNumber.objects.first()
    blog=Blog.objects.all()
    context={"blog":blog,"number":number}
    return render(request,'web/blog.html',context)


def singlepage(request,id):
    number=ContactNumber.objects.first()
    blog=Blog.objects.get(id=id)
    context={"blog":blog,"number":number}
    return render(request,'web/single-blog.html',context)
