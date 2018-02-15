from django.contrib import admin
from .models import Header


# Register your models here.

class HeaderAdmin(admin.ModelAdmin):
    fields = ['title']


admin.site.register(Header, HeaderAdmin)