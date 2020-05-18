from django.db import models

#Таблица пользователей
class Users1(models.Model):
    nickname = models.CharField(max_length=40)
    IdVK = ?
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
    sum = models.IntegerField()
    currency = (
        ('RUB')
    )
    IdPayments = ?
    status = (
        ('успешно'),
        ('не успешно')
    )

#Таблица вывода
class Output(models.Model):
    IdTrunksaction = models.ManyToManyField("Transactions")
    recipient = models.CharField()
    Sum_out =
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
