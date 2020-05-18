from django.db import models

class Human(models.Model):

    CHOICE_COMPANY = (
        ('google', 'Google'),
        ('yandex', 'Yandex'),
        ('epam', 'Epam'),
    )

    POSITION_COISES = (
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    )

    PYTHON = 'python'
    JAVA = 'java'
    CS = 'c#'
    CPP = 'c++'

    LANGUAGE_CHOISES = (
        (PYTHON, 'Python'),
        (JAVA, 'Java'),
        (CS, 'C#'),
        (CPP, 'C++'),
    )
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    birth = models.DateField(auto_now_add=False, auto_now=False)
    company = models.CharField(max_length=150, choices=CHOICE_COMPANY)
    position = models.CharField(max_length=15, choices=POSITION_COISES)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOISES, default=PYTHON)
    salary = models.IntegerField()
# Create your models here.