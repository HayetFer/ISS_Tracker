import email
from email import message
from re import sub
from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from .forms import EmailForm
from .models import Bienvenue
from django.core.mail import send_mail
from django.conf import settings


def this_mail(request):
      
    
    submitted=False
    form=EmailForm
    emails=Bienvenue.objects.all()
    if request.method=="POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            
            form.save()

            return HttpResponseRedirect('/AddMail?submitted=True')
            
        else:
            
            if 'submitted' in request.GET:
                submitted=True
    
    return render(request, 'polls/MyMail.html', {'form' : form, 'submitted':submitted, 'emails':emails})


# Create your views here.
def acceuil(request):
    response = requests.get('http://api.open-notify.org/iss-now.json')
    abc = response.json()
    isslon = abc["iss_position"]["longitude"]
    bca = response.json()
    issla = bca["iss_position"]["latitude"]
    Oceania = float(issla) > 115 and float(issla) < 150 and float(isslon) > 110 and float(isslon) < 165
    Africa = float(issla) > -35 and float(issla) < 35 and float(isslon) > -30 and float(isslon) < 65
    Eurasian = float(issla) > -10 and float(issla) < 70 and float(isslon) > -25 and float(isslon) < 180
    North_American = float(issla) > 10 and float(issla) < 70 and float(isslon) > -150 and float(isslon) < -60
    South_American = float(issla) < 10 and float(issla) > -55 and float(isslon) > -90 and float(isslon) < -30


    if North_American:
        Geolocalisation('The ISS is above the North-American region')
    if South_American:
        Geolocalisation('The ISS is above the South-American region')
    if Eurasian:
        Geolocalisation('The ISS is above the Eurasian region !')
    if Africa:
        Geolocalisation('The ISS is above the African region')
    if Oceania:
        Geolocalisation('The ISS is above the Oceanian region')
    return render(request, 'polls/Welcome.html', {'isslon': isslon, 'issla': issla})



# TODO Rename this here and in `acceuil`
def Geolocalisation(msg):
    subject = 'Welcome to TrackTheIss !'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['models.email']
    message = msg
    send_mail(subject, message, email_from, recipient_list)
    
    


def contact(request):
     return render(request, 'polls/contact.html')
        
