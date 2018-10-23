from django.contrib import admin
from FindThem.models import Disaster, Person
from django.db import models, migrations

# Register your models here
admin.site.register(Disaster)
admin.site.register(Person)
