from django.contrib import admin

from accounts.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'surname', 'email', 'phone']