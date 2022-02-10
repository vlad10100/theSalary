from django.contrib import admin

from .models import IndustryBlog

class IndustryBlogAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']

    class Meta:
        model = IndustryBlog

admin.site.register(IndustryBlog, IndustryBlogAdmin)



