from django.contrib import admin

# Register your models here.
from .models import product,contacts

admin.site.register(product)
admin.site.register(contacts)