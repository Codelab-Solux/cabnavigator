
from .models import *
from django import forms


class YearInput(forms.DateInput):
    input_type = 'year'


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class DriverExpenseForm(forms.ModelForm):
    class Meta:
        model = DriverExpense
        fields = ('__all__')
        exclude = ('date_posted', 'is_audited')
        labels = {
            'vault': 'Caisse',
            'driver': 'Conducteur',
            'title': 'Titre de la depense',
            'amount': 'Montant Payé',
            'details': 'Détails',
            'date': 'Date',
            'year': 'Année',
            'time': 'Heure',
            'receit': 'Reçu',
            'is_audited': 'Audité',
        }
        widgets = {
            'vault': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'details': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'year': YearInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class VehicleExpenseForm(forms.ModelForm):
    class Meta:
        model = VehicleExpense
        fields = ('__all__')
        exclude = ('date_posted', 'is_audited')
        labels = {
            'vault': 'Caisse',
            'vehicle': 'Véhicule',
            'title': 'Titre de la depense',
            'amount': 'Montant Payé',
            'date': 'Date',
            'year': 'Année',
            'time': 'Heure',
            'receit': 'Reçu',
            'is_audited': 'Audité',
        }
        widgets = {
            'vault': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'details': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'year': YearInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class GlobalExpenseForm(forms.ModelForm):
    class Meta:
        model = GlobalExpense
        fields = ('__all__')
        exclude = ('date_posted', 'author')
        labels = {
            'vault': 'Caisse',
            'title': 'Titre de la depense',
            'amount': 'Montant Payé',
            'details': 'Détails',
            'date': 'Date',
            'year': 'Année',
            'time': 'Heure',
            'receit': 'Reçu',
            'is_audited': 'Audité',
        }
        widgets = {
            'vault': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'details': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'year': YearInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('__all__')
        exclude = ('date_posted', 'is_audited')
        labels = {
            'vault': 'Caisse',
            'driver': 'Conducteur',
            'vehicle': 'Véhicule',
            'type': 'Type de remunération',
            'amount': 'Montant payé',
            'start_time': 'Début',
            'end_time': 'Fin',
            'is_audited': 'Audité',
        }
        widgets = {
            'vault': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'year': YearInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'start_time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'end_time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'observation': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class PayoutForm(forms.ModelForm):
    class Meta:
        model = Payout
        fields = ('__all__')
        exclude = ('date_posted', 'is_audited')
        labels = {
            'vault': 'Caisse',
            'driver': 'Conducteur',
            'vehicle': 'Véhicule',
            'type': 'Type de remunération',
            'amount': 'Montant payé',
            'title': 'Titre de la depense',
            'days_worked': 'Jours travaillés',
            'start_date': 'Début des jours travaillés',
            'end_date': 'Fin des Jours travaillés',
            'is_audited': 'Audité',
        }
        widgets = {
            'vault': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'observation': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'amount': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'days_worked': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'start_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'end_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ('__all__')
        exclude = ('date_paid',)
        labels = {
            'vault': 'Caisse',
            'partner': 'Partenaire',
            'vehicle': 'Véhicule',
            'days_worked': 'Jours travaillés',
            'gross_income': 'Gain brut',
            'net_income': 'Gain net',
            'comment': 'Commentaire',
            'is_audited': 'Audité',
            'month': 'Mois',
        }
        widgets = {
            'vault': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'partner': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'days_worked': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'gross_income': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'net_income': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'comment': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'month': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
        }


class LedgerForm(forms.ModelForm):
    class Meta:
        model = Ledger
        fields = ('__all__')
        exclude = ('is_audited',)
        labels = {
            'vault': 'Caisse',
            'details': 'Détails',
            'debit': 'Décaissement',
            'credit': 'Encaissement',
        }
        widgets = {
            'vault': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'details': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'debit': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'credit': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'year': YearInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
        }


class VaultForm(forms.ModelForm):
    class Meta:
        model = Vault
        fields = ('__all__')
        labels = {
            'type': 'Type de caisse',
            'name': 'Nom de la caisse',
            'acc_number': 'N° de compte',
            'operator': "Operateur téléphonique",
            'phone_number': 'N° de téléphone',
            'debit': 'Décaissement',
            'credit': 'Encaissement',
            'balance': 'Solde',
        }
        widgets = {
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'acc_number': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'operator': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'phone_number': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'debit': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'credit': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
            'balance': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md  border-2 border-gray-200 focus:border-black w-full"}),
        }
