from django.contrib import admin
#from .models import Transaction, Balance
from .models import Userss, InPut, Currency,Status
admin.site.register(Userss)
#admin.site.register(Payments)
# admin.site.register(Transaction)
# admin.site.register(Balance)
admin.site.register(InPut)
admin.site.register(Currency)
admin.site.register(Status)