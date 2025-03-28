from django.contrib import admin
from .models import Account, Transaction, Transfer, Bill

# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Transfer)
admin.site.register(Bill)
