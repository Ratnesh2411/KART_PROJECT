from django.contrib import admin

# Register your models here.
from .models import UserProfile,Account


admin.site.register(UserProfile)
admin.site.register(Account)
