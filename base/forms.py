
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('__all__')
        labels = {
            'name': 'Raison sociale',
            'reg_number': 'RCCM',
            'fiscal_id': 'NIF',
            'legal_status': 'Forme Juridique',
            'social_capital': 'Capital social',
            'address': 'Adresse',
            'city': 'Ville',
            'country': 'Pays',
            'phone': 'Téléphone',
            'email': 'Adresse mail',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'reg_number': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'fiscal_id': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'legal_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'social_capital': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class DocTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ('__all__')
        labels = {
            'name': 'Nom',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'description': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-xl border-2 border-gray-200 focus:border-black w-full"}),
        }


class IncidentTypeForm(forms.ModelForm):
    class Meta:
        model = IncidentType
        fields = ('__all__')
        labels = {
            'name': 'Nom',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'description': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-xl border-2 border-gray-200 focus:border-black w-full"}),
        }


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ('__all__')
        exclude = ('date_joined',)
        labels = {
            'user': 'Utilisateur',
            'civility': 'Civilité',
            'first_name': 'Prénoms',
            'last_name': 'Nom',
            'martital_status': 'Situation matrimonial',
            'nationality': 'Nationalité',
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville de résidence',
            'phone': 'Téléphone',
            'address': 'Adresse',
            'bio': 'Biographie',
        }
        widgets = {
            'user': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'commission': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'bio': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class PartnerDocumentForm(forms.ModelForm):

    class Meta:
        model = PartnerDocument
        fields = ('__all__')
        labels = {
            'user': 'Utilisateur',
            'partner': 'Partenaire',
            'type': 'Type de document',
            'issue_date': 'Délivré le',
            'expiry_date': 'Expire le',
            'issuing_country': 'Pays de délivrance',
            'is_valid': 'Validé',
        }
        widgets = {
            'partner': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'issue_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'expiry_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'issuing_country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'is_vaid': forms.BooleanField(),
        }


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('__all__')
        exclude = ('date_added', 'is_active',)
        labels = {
            'user': 'Utilisateur',
            'civility': 'Civilité',
            'first_name': 'Prénoms',
            'last_name': 'Nom',
            'martital_status': 'Situation matrimonial',
            'nationality': 'Nationalité',
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville',
            'phone': 'Téléphone',
            'address': 'Adresse',
            'bio': 'Biographie',
            'is_active': 'Actif',
        }
        widgets = {
            'user': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'score': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'bio': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),

        }


class DriverDocumentForm(forms.ModelForm):

    class Meta:
        model = DriverDocument
        fields = ('__all__')
        labels = {
            'user': 'Utilisateur',
            'driver': 'Conducteur',
            'type': 'Type de document',
            'issue_date': 'Délivré le',
            'expiry_date': 'Expire le',
            'issuing_country': 'Pays de délivrance',
            'is_valid': 'Validé',
        }
        widgets = {
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'issue_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'expiry_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'issuing_country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'is_vaid': forms.BooleanField(),
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('__all__')
        exclude = ('date_added', 'is_active')
        labels = {
            'owner': 'Propriétaire',
            'serial_number': 'Numéro de série (VIN)',
            'make': 'Marque',
            'model': 'Modèle',
            'plate_number': 'Immatriculation',
            'state': 'Etat',
            'year': 'Année de fabrication',
            'country': "Pays d'origine",
            'color': 'Couleur',
            'supplier': 'Fournisseur',
            'cost': 'Coût du véhicule',
            'commission': 'Commission(%)',
            'first_driver': 'Premier conducteur',
            'second_driver': 'Deuxieme conducteur',
            'third_driver': 'Troisieme conducteur',
        }
        widgets = {
            'owner': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'serial_number': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'make': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'model': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'plate_number': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'state': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'year': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'color': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'supplier': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'transmission': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'cost': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'commission': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'first_driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'second_driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'third_driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class VehicleDocumentForm(forms.ModelForm):

    class Meta:
        model = VehicleDocument
        fields = ('__all__')
        exclude = ('date_added',)
        labels = {
            'vehicle': 'Véhicule',
            'type': 'Type de document',
            'issue_date': 'Délivré le',
            'expiry_date': 'Expire le',
            'issuing_country': 'Pays de délivrance',
            'is_valid': 'Validé',
        }
        widgets = {
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'issue_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'expiry_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'issuing_country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'is_vaid': forms.BooleanField(),
        }


class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ('__all__')
        exclude = ('author', 'is_solved',)
        labels = {
            'title': 'Titre',
            'type': "Type d'incident",
            'driver': 'Conducteur',
            'vehicle': 'Véhicule',
            'repairability': 'Réparabilité',
            'mobility': 'Immobilisation',
            'place': "Lieu de l'incident",
            'is_solved': 'Résolu',
            'date': "Date de l'incident",
            'time': "Heure de l'incident",
        }
        widgets = {
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'mobility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'repairability': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'place': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'description': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),

        }


class TipForm(forms.ModelForm):

    class Meta:
        model = Tip
        fields = ('__all__')
        exclude = ('author', 'date_added')
        labels = {
            'title': 'Titre',
            'subtitle': "Sous titre",
            'article': 'Article',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'subtitle': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'article': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),

        }
