from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.acceuil, name='coucou'),
    path('AddMail', views.this_mail, name='mail'),
    path('contact.html', views.contact, name='contacter')
    
   
]

urlpatterns += staticfiles_urlpatterns()
