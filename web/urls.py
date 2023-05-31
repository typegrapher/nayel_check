from django.urls import path
from . import views
from django.views.static import serve


app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('career/', views.career,name='career'),
    path('contact/', views.contact,name='contact'),
    path('blog/', views.blog,name='blog'),
    
    
    path('singlepage/<int:id>', views.singlepage,name='singlepage'),
    path('career_apply/<int:id>/', views.career_apply,name='career_apply'),
    path('single_service/<int:id>/', views.single_service,name='single_service'),
]