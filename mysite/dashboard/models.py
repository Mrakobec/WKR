from django.db import models
from django.contrib.auth.models import User

class Userss(models.Model):
    nickname = models.CharField(max_length=20)
    socialauth = models.OneToOneField(User,  on_delete=models.CASCADE)
    def __str__(self):
        return (self.nickname)

class Currency(models.Model):
    currency_type = (
        ('1', 'РУБЛИ'),
        ('2', 'EURO'),
    )
    name = models.CharField(max_length=20 # choices=currency_type, default='1'
     )

    def __str__(self):
        return (self.name)

class Status(models.Model):
    # SUCCESS = 'УСП'
    # # UNSUCCESS = 'НЕУСП'
    # currency_type = (
    #     ('2', 'успешно'),
    #     ('1', 'неуспешно'),
    # )
    name = models.CharField(max_length=20)

    def __str__(self):
        return (self.name)

class Payment_Method(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return (self.name)



class InPut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    comiss1 = models.DecimalField(decimal_places=2,  max_digits=10)
    comiss2 = models.DecimalField(decimal_places=2, max_digits=10)
    comiss_end = models.DecimalField(decimal_places=2, max_digits=10)
    amount_end = models.DecimalField(decimal_places=2, max_digits=10)
    text = models.CharField(max_length=250)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    def __str__(self):
        return (self.name)



class OutPut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    payment_method = models.ForeignKey(Payment_Method, on_delete=models.PROTECT)
    comiss = models.DecimalField(decimal_places=2, max_digits=10)
    amount_end = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    def __str__(self):
        return (self.recipient)

class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    input = models.DecimalField(decimal_places=2, max_digits=10)
    output = models.DecimalField(decimal_places=2, max_digits=10)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    def __int__(self):
        return (self.id)

