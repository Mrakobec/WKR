# Generated by Django 3.0.6 on 2020-05-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200529_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
