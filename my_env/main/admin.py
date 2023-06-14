from django.contrib import admin

# Register your models here.

from .models import Recipient

admin.site.register(Recipient)
