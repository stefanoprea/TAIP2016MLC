from django.contrib import admin

# Register your models here.
from .models import Wordpair,Mysession

admin.site.register(Wordpair)
admin.site.register(Mysession)