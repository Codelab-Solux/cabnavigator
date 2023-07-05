from django.db import models
from base.models import *

# Create your models here.


class DriverExpense(models.Model):
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
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.driver.first_name} ({self.title} - {self.amount})'

    def get_absolute_url(self):
        return reverse('driver_expense', kwargs={'pk': self.pk})


class VehicleExpense(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    details = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.IntegerField(null=False, blank=True, default='0')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    is_audited = models.BooleanField(default=False)
    receit = models.ImageField(
        upload_to='vehicle_expenses', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.vehicle.make}[-{self.vehicle.plate_number}-] - ({self.title}) - [{self.amount}]'

    def get_absolute_url(self):
        return reverse('vehicle_expense', kwargs={'pk': self.pk})


class GlobalExpense(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    details = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.IntegerField(null=False, blank=True, default='0')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    is_audited = models.BooleanField(default=False)
    receit = models.ImageField(
        upload_to='global_expenses', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.first_name} ({self.title}) - [{self.amount}]'

    def get_absolute_url(self):
        return reverse('global_expense', kwargs={'pk': self.pk})


class Payment(models.Model):
    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=True, default='0')
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    date_paid = models.DateTimeField(auto_now=True)
    is_audited = models.BooleanField(default=False)

    # receit = models.ImageField(
    #     upload_to='driver_expenses', blank=True, null=True)

    def __str__(self):
        return f'{self.driver.first_name} - [{self.amount}]'

    def get_absolute_url(self):
        return reverse('payment', kwargs={'pk': self.pk})


payout_types = (
    ('salary', 'Salaire'),
    ('sabbatic', 'Paiement autonome sabbatique'),
)


class Payout(models.Model):
    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True)
    days_worked = models.IntegerField(default='0',)
    amount = models.IntegerField(null=False, blank=True, default='0')
    type = models.CharField(
        max_length=50, default='salary', choices=payout_types)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    date_paid = models.DateTimeField(auto_now=True)
    is_audited = models.BooleanField(default=False)

    # receit = models.ImageField(
    #     upload_to='driver_expenses', blank=True, null=True)

    def __str__(self):
        return f'{self.driver.first_name} - [{self.amount}]'

    def get_absolute_url(self):
        return reverse('payout', kwargs={'pk': self.pk})


class Dividend(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    days_worked = models.IntegerField(default='0',)
    gross_income = models.IntegerField(default='0', null=False, blank=True,)
    net_income = models.IntegerField(default='0', null=False, blank=True,)
    comment = models.TextField(null=False, blank=True)
    date_paid = models.DateTimeField(auto_now=True)
    is_audited = models.BooleanField(default=False)

    def __str__(self):
        return f'({self.vehicle.plate_number}) - [{self.gross_income}]'

    def get_absolute_url(self):
        return reverse('dividend', kwargs={'pk': self.pk})


class Revenue(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    days_worked = models.IntegerField(default='0',)
    gross_income = models.IntegerField(default='0', null=False, blank=True,)
    net_income = models.IntegerField(default='0', null=False, blank=True,)
    comment = models.TextField(null=False, blank=True)
    date_paid = models.DateTimeField(auto_now=True)
    is_audited = models.BooleanField(default=False)

    def __str__(self):
        return f'({self.vehicle.plate_number}) - [{self.gross_income}]'

    def get_absolute_url(self):
        return reverse('revenue', kwargs={'pk': self.pk})

