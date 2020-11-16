

# Register your models here.
from django.contrib import admin
from .models import Picture, Category, Location



admin.site.register(Picture)
admin.site.register(Category)
admin.site.register(Location)