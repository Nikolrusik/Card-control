from django.db import models
from dateutils import relativedelta
from datetime import datetime


class CardsModel(models.Model):
    STATUS_CHOICES = (
        ('ACTIVATE', 'Активирована'),
        ('NOT_ACTIVATE', 'Не активирована'),
        ('OVERDUE', 'Просрочена')
    )

    ENDDATE_CHOICES = (
        (datetime.now() + relativedelta(years=1), 'Year'),
        (datetime.now() + relativedelta(months=6), '6 months'),
        (datetime.now() + relativedelta(months=1), '1 month')
    )

    series = models.CharField(verbose_name="Seria")
    number = models.CharField(verbose_name="Number")
    release_date = models.DateTimeField(
        verbose_name="Release date", auto_now_add=True)
    end_date = models.DateTimeField(
        verbose_name="Release date", default=datetime.now + relativedelta(years=1), choices=ENDDATE_CHOICES)
    used_date = models.DateTimeField(
        verbose_name="Release date", auto_now_add=True, auto_now=True)
    balance = models.DecimalField(verbose_name="Balace", default=0)
    status = models.CharField(choices=STATUS_CHOICES)


class HistoryCardModel(models.Model):
    card = models.ForeignKey(CardsModel, on_delete=models.CASCADE)
    place_purshace = models.CharField(verbose_name="Place of purshace")
    purshace_amount = models.DecimalField(verbose_name="Purshace ampunt")
