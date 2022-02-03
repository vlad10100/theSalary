from django.contrib import admin

from .models import CustomUser, UserProfile

from datetime import datetime

admin.site.register(CustomUser)


class UserProfileAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated', 'user')
    readonly_fields = ['created', 'updated']

    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)