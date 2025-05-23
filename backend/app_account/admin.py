from django.contrib import admin
from .models import User, Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "country"]


admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)
