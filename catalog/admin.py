from django.contrib import admin

# Register your models here.
from .models import Person, School, Lessons

admin.site.register(Lessons)
admin.site.register(Person)
admin.site.register(School)