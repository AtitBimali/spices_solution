import email
from django.db import models

# Create your models here.
class Industry(models.Model):
    industry_type = models.CharField(primary_key=True,max_length=150)
    
    def __str__(self):
        return self.industry_type


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=50)
    industry_type = models.ForeignKey('Industry',on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

