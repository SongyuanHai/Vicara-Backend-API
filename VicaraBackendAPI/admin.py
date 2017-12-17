from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.TimeSheet)
admin.site.register(models.ProjectMaster)