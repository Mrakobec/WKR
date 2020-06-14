from django.contrib import admin
#from .models import Transaction, Balance
from django.contrib.auth.models import User
from .models import *

#admin.site.register(Payments)
# admin.site.register(Transaction)
# admin.site.register(Balance)
# admin.site.register(Subscriber)
class InPutAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'date',
                    'name',
                    'amount',
                    'currency',
                    'comiss1',
                    'comiss2',
                    'comiss_end',
                    'amount_end',
                    'text',
                    'status')
    search_fields = ['user__username', 'id', 'name']
    pass
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'input',
                    'output',
                    'balance',
                    'currency')
    search_fields = ['user__username', 'id']
    pass
class OutPutAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'recipient',
                    'date',
                    'amount',
                    'currency',
                    'payment_method',
                    'comiss',
                    'amount_end',
                    'status')
    search_fields = ['user__username', 'id', 'recipient']
    pass
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')
    search_fields = ['name', 'id']
    pass
class Payment_MethodAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')
    search_fields = ['name', 'id']
    pass
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')
    search_fields = ['name', 'id']
    pass

admin.site.register(InPut, InPutAdmin)
admin.site.register(OutPut, OutPutAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Payment_Method, Payment_MethodAdmin)


admin.site.site_header = 'Admin panel'
admin.site.site_title = 'Admin panel'