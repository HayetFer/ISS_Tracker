from django.db import models
from django.contrib.auth.models import User

class Bienvenue(models.Model):
    mail = models.EmailField()
    

    def __str__(self):
        return self.mail
    


# Create your models here.
