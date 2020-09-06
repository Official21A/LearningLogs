from django.contrib import admin

# Register your models here.

from .models import Topic, Entry

# while working with django registering the objects is nessecury
admin.site.register(Topic)
admin.site.register(Entry)
