from django.contrib import admin

# Register your models here.
from .models import SalesOrder

admin.site.register(SalesOrder)
