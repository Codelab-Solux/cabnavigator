from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *


# @receiver(post_save, sender=DriverExpense)
def DriverExpenseTransaction(sender, instance, created, **kwargs):
    if created:
        DriverExpense = instance
        transaction = Transaction.objects.create()

    print('Driver Transaction created from signal')


post_save.connect(DriverExpenseTransaction, sender=DriverExpense)


@receiver(post_save, sender=VehicleExpense)
def create_expense_ledger(sender, instance, created, **kwargs):
    if created:
        Ledger.objects.create(
            vehicle=instance.vehicle,
            details=instance.title,
            debit=instance.amount,
            credit=0,
            date=instance.date,
            is_audited=instance.is_audited,
        )
        print('Vehicle ledger created from signal')


# post_save.connect(create_expense_ledger, sender=VehicleExpense)

@receiver(post_save, sender=VehicleExpense)
def edit_expense_ledger(sender, instance, created, **kwargs):
    if created == False:
        Ledger.objects.update(
            vehicle=instance.vehicle,
            details=instance.title,
            debit=instance.amount,
            credit=0,
            date=instance.date,
            is_audited=instance.is_audited,
        )
        print('Expense ledger edited from signal')


# post_save.connect(edit_expense_ledger, sender=VehicleExpense)

# -------------------------------- payment signals------------------------------------------


@receiver(post_save, sender=Payment)
def create_payment_ledger(sender, instance, created, **kwargs):
    if created:
        Ledger.objects.create(
            vehicle=instance.vehicle,
            details="Payment du jour",
            credit=instance.amount,
            debit=0,
            date=instance.date_paid,
            is_audited=instance.is_audited,
        )
        print('Payment ledger created from signal')


# post_save.connect(create_payment_ledger, sender=Payment)

@receiver(post_save, sender=Payment)
def edit_payment_ledger(sender, instance, created, **kwargs):
    if created == False:
        Ledger.objects.update(
            vehicle=instance.vehicle,
            details="Payment du jour",
            credit=instance.amount,
            debit=0,
            date=instance.date_paid,
            is_audited=instance.is_audited,
        )
        print('Expense ledger edited from signal')


# post_save.connect(edit_payment_ledger, sender=Payment)
