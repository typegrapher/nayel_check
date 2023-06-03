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


# def career_apply(request,id):
#     number=ContactNumber.objects.first()
#     career=Career.objects.get(id=id)
#     context={"career":career,"number":number}
    
#     if request.method == 'POST':
#         name = request.POST.get('Name')
#         email = request.POST.get('Email')
#         phone = request.POST.get('Phone')
#         message = request.POST.get('Message')
#         qualification = request.POST.get('Qualification')
#         career = request.POST.get('Career')

#         if qualification:  # Check if qualification is not empty
#             careers = CareerApply(
#                 name=name,
#                 email=email,
#                 phone=phone,
#                 message=message,
#                 qualification=qualification,
#                 career=career,
#             )
#             careers.save()


#         email_template = render_to_string('web/email_career.html', {
#             'name': name,
#             'phone': phone,
#             'email': email,
#             'message': message,
#             'qualification': qualification,
#             'career': career,
#         })
#         # Send the email
#         send_mail(
#             'Nayel career apply',
#             '',
#             settings.DEFAULT_FROM_EMAIL,
#             ['kfaamardesubombhack@gmail.com'],
#             html_message=email_template,
#             fail_silently=False,
#         )

#         return render(request,"web/career-apply.html",context)

        
#     return render(request,"web/career-apply.html",context)


import gspread 
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import os

def career_apply(request, id):
    number = ContactNumber.objects.first()
    career = Career.objects.get(id=id)
    context = {"career": career, "number": number}

    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        message = request.POST.get('Message')
        qualification = request.POST.get('Qualification')
        career = request.POST.get('Career')

        # if qualification:  # Check if qualification is not empty
        careers = CareerApply(
            name=name,
            email=email,
            phone=phone,
            message=message,
            qualification=qualification,
            career=career,
        )
        careers.save()

            # Send data to Google Sheet
        
        (name, email, phone, message, qualification, career)

        # Send email
        send_email(name, email, phone, message, qualification, career)

        return render(request, "web/career-apply.html", context)

    return render(request, "web/career-apply.html", context)


def send_to_google_sheet(name, email, phone, message, qualification, career):
    # Replace 'SHEET_ID' with the actual ID of your Google Sheet
    # sheet_id = '1t5GtE9cYmwpo8vOaCg9YkV0MmFUo9FNIDsXk95GNYOE'
    
    # Define the scope and credentials for Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive',
             'https://www.googleapis.com/auth/spreadsheets']
    
    # json_keyfile = os.path.join(BASE_DIR, 'static/web/credentials/careerapply-a2e02e23710a.json')
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/static/web/credentials/django-sendsheet-e71501508a2b.json', scope)

    # Authorize the client and open the Google Sheet
    client = gspread.authorize(credentials)
    # sheet = client.open_by_key(sheet_id).sheet1
    sheet = client.create('sendtosheet').sheet1
    sheet.share('kfaamardesubombhack@gmail.com', perm_type = 'user' , role = 'writer')


    # Prepare the data to be inserted
    data = [name, email, phone, message, qualification, career]

    # Append the data to the Google Sheet
    sheet.append_row(data)


def send_email(name, email, phone, message, qualification, career):
    email_template = render_to_string('web/email_career.html', {
        'name': name,
        'phone': phone,
        'email': email,
        'message': message,
        'qualification': qualification,
        'career': career,
    })

    send_mail(
        'Nayel career apply',
        '',
        settings.DEFAULT_FROM_EMAIL,
        ['kfaamardesubombhack@gmail.com'],
        html_message=email_template,
        fail_silently=False,
    )



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
