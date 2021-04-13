from django.contrib import admin
from .models import User # User from model.py class

# Register your models here.
admin.site.register(User)