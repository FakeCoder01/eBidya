from asyncio import streams
from dataclasses import fields
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class user(models.Model):

    #GENERAL 
    gender = models.CharField(max_length=8)
    username = models.CharField(max_length=50)
    current_education = models.CharField(max_length=8)
    stream =  models.CharField(max_length = 16)
    educational_institution = models.CharField(max_length=100)
    target_exam = models.CharField(max_length=8)

    #ADDRESS
    pincode = models.IntegerField(max_length=6)
    city = models.CharField(max_length = 16)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length = 16)

    #CONTACT
    phone = models.IntegerField(max_length=13)
    email  = models.EmailField()

    #SYSTEM
    userid = models.CharField(max_length=8)
    otp = models.IntegerField(max_length=6)
    password_hash = models.CharField(max_length=100)
    hash = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    mobile_verify = models.CharField(max_length=8)
    email_verify = models.CharField(max_length=8)
    token = models.CharField(max_length=100)

    #SUBSCRIPTION
    jee_subid = models.CharField(max_length = 16)
    neet_subid = models.CharField(max_length = 16)
    board_subid = models.CharField(max_length = 16)
    upsc_subid = models.CharField(max_length = 16)
    cat_subid = models.CharField(max_length = 16)
    progm_subid = models.CharField(max_length = 16)
    psu_subid = models.CharField(max_length = 16)