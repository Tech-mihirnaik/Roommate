from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.bookedCab)
admin.site.register(models.cabowner)
admin.site.register(models.driver)
admin.site.register(models.addcab)