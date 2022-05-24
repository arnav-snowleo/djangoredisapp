from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Recipe)

#superuser name 'arnav'
#pw - 'password1234'