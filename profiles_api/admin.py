from django.contrib import admin
from profiles_api import models

#Register your models here
#adding them to admin portal
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
