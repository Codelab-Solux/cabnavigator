from django.db import models
from base.models import *

from base.utils import h_encode, h_decode
from month.models import MonthField

# Create your models here.


vault_types = (
    ('cash', 'Physique'),
    ('mobile', 'Mobile'),
    ('bank', 'Bancaire'),
)


class Vault(models.Model):
    type = models.CharField(
        max_length=50, choices=vault_types)
    #
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    acc_number = models.CharField(max_length=255, null=False, blank=True)
    operator = models.CharField(max_length=255, null=False, blank=True)
    phone_number = models.CharField(
        max_length=255, null=False, blank=True, unique=True)
    #
    debit = models.IntegerField(null=False, blank=True, default='0')
    credit = models.IntegerField(null=False, blank=True, default='0')
    balance = models.IntegerField(null=False, blank=True, default='0')

    def __str__(self):
        return f'{self.type} ({self.debit} - {self.credit})'

    

    def get_hashid(self):
        return h_encode(self.id)

    def get_absolute_url(self):
        return reverse('mobile_vault', kwargs={'pk': self.pk})


class Ledger(models.Model):
    vault = models.ForeignKey(
        Vault, on_delete=models.SET_NULL, null=True, blank=True)
    details = models.CharField(max_length=1000, blank=True, null=True)
    debit = models.IntegerField(null=False, blank=True, default='0')
    credit = models.IntegerField(null=False, blank=True, default='0')
    date = models.DateField(null=True, blank=True)
    is_audited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.vault} [{self.credit} - {self.debit}]'

    

    def get_hashid(self):
        return h_encode(self.id)

    def get_absolute_url(self):
        return reverse('ledger', kwargs={'pk': self.pk})


class DriverExpense(models.Model):
    vault = models.ForeignKey(
        Vault, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, default='')
    details = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.IntegerField(null=False, blank=True, default='0')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    is_audited = models.BooleanField(default=False)
    receit = models.ImageField(
        upload_to='driver_expenses', blank=True, null=True)

    def __str__(self):
        return f'{self.driver.first_name} ({self.title} - {self.amount})'

    

    def get_hashid(self):
        return h_encode(self.id)

    def get_absolute_url(self):
        return reverse('driver_expense', kwargs={'pk': self.pk})


class VehicleExpense(models.Model):
    vault = models.ForeignKey(
        Vault, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    details = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.IntegerField(null=False, blank=True, default='0')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    is_audited = models.BooleanField(default=False)
    receit = models.ImageField(
        upload_to='vehicle_expenses', blank=True, null=True)

    def __str__(self):
        return f'{self.vehicle.make}[-{self.vehicle.plate_number}-] - ({self.title}) - [{self.amount}]'

    

    def get_hashid(self):
        return h_encode(self.id)

    def get_absolute_url(self):
        return reverse('vehicle_expense', kwargs={'pk': self.pk})


class GlobalExpense(models.Model):
    vault = models.ForeignKey(
        Vault, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    details = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.IntegerField(null=False, blank=True, default='0')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    is_audited = models.BooleanField(default=False)
    receit = models.ImageField(
        upload_to='global_expenses', blank=True, null=True)

    def __str__(self):
        return f'{self.author.first_name} ({self.title}) - [{self.amount}]'

    

    def get_hashid(self):
        return h_encode(self.id)

    def get_absolute_url(self):
        return reverse('global_expense', kwargs={'pk': self.pk})


class Payment(models.Model):
    vault = models.ForeignKey(
        Vault, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=True, default='0')
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    payday = models.DateTimeField(auto_now=True)
    is_audited = models.BooleanField(default=False)

    # receit = models.ImageField(
    #     upload_to='driver_expenses', blank=True, null=True)

    def __str__(self):
        return f'{self.driver.first_name} - [{self.amount}]'

    

    def get_hashid(self):
        return h_encode(self.id)

    def get_absolute_url(self):
        return reverse('payment', kwargs={'pk': self.pk})


payout_types = (
    ('salary', 'Salaire'),
    ('sabbatic', 'Paiement autonome sabbatique'),
)


class Payout(models.Model):
    vault = models.ForeignKey(
        Vault, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True)
    days_worked = models.IntegerField(default='0',)
    amount = models.IntegerField(null=False, blank=True, default='0')
    type = models.CharField(
        max_length=50, default='salary', choices=payout_types)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    payday = models.DateTimeField(auto_now=True)
    is_audited = models.BooleanField(default=False)

    # receit = models.ImageField(
    #     upload_to='driver_expenses', blank=True, null=True)

    def __str__(self):
        return f'{self.driver.first_name} - [{self.amount}]'

    

    def get_hashid(self):
        return h_encode(self.id)

    def get_absolute_url(self):
        return reverse('payout', kwargs={'pk': self.pk})


class Revenue(models.Model):
    vault = models.ForeignKey(
        Vault, on_delete=models.SET_NULL, null=True, blank=True)
    partner = models.ForeignKey(
        Partner, on_delete=models.SET_NULL, null=True, blank=True,)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    days_worked = models.IntegerField(default='0',)
    gross_income = models.IntegerField(default='0', null=False, blank=True,)
    net_income = models.IntegerField(default='0', null=False, blank=True,)
    comment = models.TextField(null=False, blank=True)
    payday = models.DateTimeField(auto_now=True)
    month = MonthField("Mois", null=True, blank=True,)
    is_audited = models.BooleanField(default=False)

    def __str__(self):
        return f'({self.vehicle.plate_number}) - [{self.gross_income}]'

    

    def get_hashid(self):
        return h_encode(self.id)

    def get_absolute_url(self):
        return reverse('revenue', kwargs={'pk': self.pk})
