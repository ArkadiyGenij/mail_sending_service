from django.contrib import admin

from mail_sending.models import Message, Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    ordering = ('name',)
    search_fields = ('name','email')