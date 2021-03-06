from tabnanny import verbose
from tokenize import blank_re
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True)

    def __str__(self):
        if self.phone and self.email:
            return "{}, {}, {}".format(self.company_name, self.phone, self.email)
        else:
            return "{}".format(self.company_name)


    class Meta:
        verbose_name_plural = "Companies"