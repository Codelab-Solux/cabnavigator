
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
            'details': 'Raisons',
            'date': 'Date',
            'time': 'Heure',
            'receit': 'Reçu',
        }
        widgets = {
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'details': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
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
            'details': 'Raisons',
            'date': 'Date',
            'time': 'Heure',
            'receit': 'Reçu',
        }
        widgets = {
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'details': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
        }


class GlobalExpenseForm(forms.ModelForm):
    class Meta:
        model = GlobalExpense
        fields = ('__all__')
        exclude = ('date_posted', 'author')
        labels = {
            'title': 'Titre de la depense',
            'amount': 'Montant Payé',
            'details': 'Raisons',
            'date': 'Date',
            'time': 'Heure',
            'receit': 'Reçu',
        }
        widgets = {
            # 'author': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'details': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
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
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'start_time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'end_time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'observation': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
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
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'observation': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'days_worked': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'start_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'end_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
        }

class DividendForm(forms.ModelForm):
    class Meta:
        model = Dividend
        fields = ('__all__')
        exclude = ('date_paid',)
        labels = {
            'partner': 'Partenaire',
            'vehicle': 'Véhicule',
            'days_worked': 'Jours travaillés',
            'gross_income': 'Gain brut',
            'net_income': 'Gain net',
            'comment': 'Commentaire',
            'is_audited': 'Audité',
        }
        widgets = {
            'partner': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'days_worked': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'gross_income': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'net_income': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'comment': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            # 'is_audited': forms.BooleanField(required=True)
        }
