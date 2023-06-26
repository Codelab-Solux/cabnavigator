
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class DriverExpenseForm(forms.ModelForm):
    class Meta:
        model = DriverExpense
        fields = ('__all__')
        exclude = ('date_posted',)
        labels = {
            'driver': 'Conducteur',
            'title': 'Titre de la depense',
            'amount': 'Montant Payé',
            'motive': 'Raisons',
            'date': 'Date',
            'time': 'Heure',
            'receit': 'Reçu',
        }
        widgets = {
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'motive': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class VehicleExpenseForm(forms.ModelForm):
    class Meta:
        model = VehicleExpense
        fields = ('__all__')
        exclude = ('date_posted',)
        labels = {
            'vehicle': 'Véhicule',
            'title': 'Titre de la depense',
            'amount': 'Montant Payé',
            'motive': 'Raisons',
            'date': 'Date',
            'time': 'Heure',
            'receit': 'Reçu',
        }
        widgets = {
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'motive': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class GlobalExpenseForm(forms.ModelForm):
    class Meta:
        model = GlobalExpense
        fields = ('__all__')
        exclude = ('date_posted',)
        labels = {
            'author': 'Autheur',
            'title': 'Titre de la depense',
            'amount': 'Montant Payé',
            'motive': 'Raisons',
            'date': 'Date',
            'time': 'Heure',
            'receit': 'Reçu',
        }
        widgets = {
            'author': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'motive': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('__all__')
        exclude = ('date_posted',)
        labels = {
            'driver': 'Conducteur',
            'vehicle': 'Véhicule',
            'type': 'Type de remunération',
            'amount': 'Montant payé',
            'start_time': 'Début',
            'end_time': 'Fin',
        }
        widgets = {
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'start_time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'end_time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'observation': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class PayoutForm(forms.ModelForm):
    class Meta:
        model = Payout
        fields = ('__all__')
        exclude = ('date_posted',)
        labels = {
            'driver': 'Conducteur',
            'vehicle': 'Véhicule',
            'type': 'Type de remunération',
            'amount': 'Montant payé',
            'title': 'Titre de la depense',
            'days_worked': 'Jours travaillés',
            'start_date': 'Début des jours travaillés',
            'end_date': 'Fin des Jours travaillés',
        }
        widgets = {
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'observation': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'days_worked': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'start_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'end_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class LedgerForm(forms.ModelForm):
    class Meta:
        model = Ledger
        fields = ('__all__')
        exclude = ('date_posted',)
        labels = {
            'vehicle': 'Véhicule',
            'debit': 'Décaissement',
            'credit': 'Encaissement',
            'details': 'Détails',
            'profit': 'Gains net',
            'start_date': 'Début',
            'end_date': 'Fin',
        }
        widgets = {
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'details': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'debit': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'credit': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'profit': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'end_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }
