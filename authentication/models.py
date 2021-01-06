from django.db import models

# Create your models here.
class SignUp(models.Model):   
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)