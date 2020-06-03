from django.contrib import admin
#from .models import Transaction, Balance
from .models import InPut, Currency,Status, Balance, OutPut, Payment_Method, Subscriber

#admin.site.register(Payments)
# admin.site.register(Transaction)
# admin.site.register(Balance)
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
    pass
admin.site.register(InPut, InPutAdmin)
admin.site.register(OutPut)
admin.site.register(Balance)
admin.site.register(Currency)
admin.site.register(Status)
admin.site.register(Payment_Method)
admin.site.register(Subscriber)

admin.site.site_header = 'Admin panel'
admin.site.site_title = 'Admin panel'