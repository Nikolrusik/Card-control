from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import datetime
from authapp.models import AbstractUserModel


class CardsModel(models.Model):
    STATUS_CHOICES = (
        ('ACTIVATE', 'Активирована'),
        ('NOT_ACTIVATE', 'Не активирована'),
        ('OVERDUE', 'Просрочена')
    )

    user = models.ForeignKey(AbstractUserModel, on_delete=models.CASCADE)
    series = models.CharField(verbose_name="Seria", max_length=4)
    number = models.CharField(verbose_name="Number", max_length=16)
    release_date = models.DateTimeField(
        verbose_name="Release date", auto_now_add=True)
    end_date = models.DateTimeField(
        verbose_name="End date", default=datetime.now() + relativedelta(year=1))
    used_date = models.DateTimeField(
        verbose_name="Used date", auto_now=True)
    balance = models.DecimalField(
        verbose_name="Balace", default=0, decimal_places=2, max_digits=5)
    status = models.CharField(choices=STATUS_CHOICES, max_length=150)


class HistoryCardModel(models.Model):
    card = models.ForeignKey(CardsModel, on_delete=models.CASCADE)
    place_purshace = models.CharField(
        verbose_name="Place of purshace", max_length=50)
    purshace_amount = models.DecimalField(
        verbose_name="Purshace ampunt", max_digits=5.2, decimal_places=3)
