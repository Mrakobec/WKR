from django.db import models
#
# #Таблица пользователей
# class Users1(models.Model):
#     nickname = models.CharField(max_length=40)
#     IdVK = models.IntegerField()
# #Таблица поступивших пожертвований
# class Payments(models.Model):
#     IdUser = models.ManyToManyField("Users1")
#     name = models.CharField(max_length=40)
#     sum_in = models.ForeignKey
#     comission = models.FloatField()
#     #our_comission = sum_in*0.01
#     text = models.TextField()
#     date_payment = models.DateField()
#     IdTrunksaction = models.ManyToManyField("Transactions")
#
# #Таблица транзакций
# class Transaction:
#     currency = (
#         ('RUB', 'РУБЛИ'),
#         ('EUR', 'EURO')
#     )
#     status = (
#         ('УСП', 'Успешно'),
#         ('НЕУСП','Неуспешно')
#     )
#     sum = models.IntegerField()
#     currency = models.CharField(max_length=20, choices=currency)
#     IdPayments = models.IntegerField()
#     status = models.CharField(max_length=20, choices=status)
#
# #Таблица вывода
# class Output(models.Model):
#     status = (
#         ('успешно'),
#         ('не успешно')
#     )
#     system_out = (
#         ('Банковский счёт'),
#         ('VK Pay')
#     )
#     IdTrunksaction = models.ManyToManyField("Transactions")
#     recipient = models.CharField()
#     Sum_out = models.IntegerField()
#     system_out = models.CharField(max_length=50, choices=system_out)
#     date_payment = models.DateField()
#     status = models.CharField (max_length=20, choices=status)
#
# #Таблица баланся?
# class Balance(models.Model):
#     IdUser = models.ManyToManyField("Users1")
#     sum_in = models.ManyToManyField("Payments")
#     sum_out = models.ManyToManyField("Output")
#     comiss_bank = models.IntegerField()
#     comiss_our = models.IntegerField()
#     balance = models.IntegerField()

class Userss(models.Model):
    nickname = models.CharField(max_length=20)

class Currency(models.Model):
    currency_type = (
        ('RUB', 'РУБЛИ'),
        ('EUR', 'EURO'),
    )
    name = models.CharField(max_length=20, choices=currency_type, default='RUB')

class Status(models.Model):
    SUCCESS = 'УСП'
    UNSUCCESS = 'НЕУСП'
    name = (
        (SUCCESS, 'успешно'),
        (UNSUCCESS, 'неуспешно')
    )

class InPut(models.Model):
    user = models.ForeignKey(Userss, on_delete=models.CASCADE)
    date = models.DateTimeField()
    name = models.CharField(max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    comiss1 = models.DecimalField(decimal_places=2, max_digits=10)
    comiss2 = models.DecimalField(decimal_places=2, max_digits=10)
    amount_end = models.DecimalField(decimal_places=2, max_digits=10)
    text = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

class OutPut(models.Model):
    user = models.ForeignKey(Userss, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=50)
    date = models.DateTimeField()
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    payment_method = models.CharField(max_length=50)
    comiss3 = models.DecimalField(decimal_places=2, max_digits=10)
    amount_end = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

class Balance(models.Model):
    user = models.OneToOneField(Userss, on_delete=models.CASCADE)
    input = models.DecimalField(decimal_places=2, max_digits=10)
    output = models.DecimalField(decimal_places=2, max_digits=10)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
# # Create your models here.
