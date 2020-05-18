from django.db import models

#Таблица пользователей
class Users1(models.Model):
    nickname = models.CharField(max_length=40)
    IdVK = models.IntegerField()
#Таблица поступивших пожертвований
class Payments(models.Model):
    IdUser = models.ManyToManyField("Users1")
    name = models.CharField(max_length=40)
    sum_in = models.ForeignKey
    text = models.TextField
    date_payment = models.DateField()
    IdTrunksaction = models.ManyToManyField("Transactions")

#Таблица транзакций
class Transaction:
    currency = (
        ('RUB', 'РУБЛИ'),
        ('EUR', 'EURO')
    )
    status = (
        ('УСП', 'Успешно'),
        ('НЕУСП','Неуспешно')
    )
    sum = models.IntegerField()
    currency = models.CharField(max_length=20, choices=currency)
    IdPayments = models.IntegerField()
    status = models.CharField(max_length=20, choices=status)

#Таблица вывода
class Output(models.Model):
    IdTrunksaction = models.ManyToManyField("Transactions")
    recipient = models.CharField()
    Sum_out = models.IntegerField()
    system_out = (
        ('Банковский счёт'),
        ('VK Pay')
    )
    date_payment = models.DateField()
    status = (
        ('успешно'),
        ('не успешно')
    )
#Таблица баланся?
class Balance(models.Model):
    IdUser = models.ManyToManyField("Users1")
    sum_in = models.ManyToManyField("Payments")
    sum_out = models.ManyToManyField("Output")
    comiss_bank = models.IntegerField()
    comiss_our = models.IntegerField()
    balance = models.IntegerField()
# Create your models here.
