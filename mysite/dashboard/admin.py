from django.contrib import admin
#from .models import Transaction, Balance
from .models import InPut, Currency,Status, Balance, OutPut, Payment_Method

#admin.site.register(Payments)
# admin.site.register(Transaction)
# admin.site.register(Balance)
admin.site.register(InPut)
admin.site.register(OutPut)
admin.site.register(Balance)
admin.site.register(Currency)
admin.site.register(Status)
admin.site.register(Payment_Method)