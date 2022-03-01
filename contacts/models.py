from enum import unique
from random import choices
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

#Validators
mobile_validator = RegexValidator(r"^((\+){1}91){1}[1-9]{1}[0-9]{9}$")

def source_validator(self):
        pass




# Model Tables


class Contact(models.Model):

    gender_choices = (
        ("NA", _("Rather not say")),
        ("M",_("Male")),
        ("F",_("Female"))
    )

    marital_status_choices = (
        ("S","Single"),
        ("M","Married"),
        ("U","Unmarried"),
        ("D","Divorced")
    )
    #Demographic Fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True)
    gender = models.CharField(choices=gender_choices,max_length=2,blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    marital_status = models.CharField(choices=marital_status_choices,blank=True,max_length=1,null=True)

    #address details
    address_type_choices = (
        ("P","Permanent"),
        ("W","Work"),
        ("O","Other")
    )
    address_type = models.CharField(choices=address_type_choices,default="P",max_length=1)
    address = models.CharField(max_length=300,blank=True,null=True)
    
    # virtual addresses
    mobile = models.CharField(validators= [mobile_validator] ,help_text = _("Mobile NO: +9185XXXXXXXX"),unique=True,max_length=13)
    secondary_mobile = models.CharField(validators= [mobile_validator] ,help_text=_("Mobile NO: +9185XXXXXXXX"),max_length=13,null=True)
    email = models.EmailField(_("Type your email address"),unique=True)

    #  important fields
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)  #This will be changed each time the contact object is changed


    #This should be taken care of because we have to assign it to admin user when deleted
    owner = models.ForeignKey(User,on_delete=models.SET_DEFAULT,default=1)

    source_choices = (
        ("MyMarket","MyMarket"),
    )
    source = models.CharField(max_length=30, choices=source_choices,null=True)
    

