from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Wordpair(models.Model):
    text=models.CharField(max_length=200,unique=True)
    votes=models.CharField(max_length=200,
        validators=["validate_comma_separated_integer_list"],
        default="0,0,0,0,0")
    nrvotes=models.IntegerField(default=0)
    #begun=models.BooleanField(default=False)
    finished=models.BooleanField(default=False)
    preferred=models.BooleanField(default=False)
    #date_last_voted=models.DateTimeField('date last voted')
    __str__=lambda self:self.text

class Mysession(models.Model):
    sessionkey=models.CharField(max_length=100,default="foo")
    wordpairs=models.ManyToManyField(Wordpair)

