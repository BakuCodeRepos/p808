from django.contrib import admin

from .models import Account, SubscribedUser


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'get_full_name')


admin.site.register(SubscribedUser)
