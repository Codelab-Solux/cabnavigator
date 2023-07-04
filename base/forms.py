
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class PartnerCreateForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ('__all__')
        exclude = ('bio',)
        labels = {
            'user': 'Utilisateur',
            'contract': 'Contrat',
            'nationality': 'Nationalité',
            'civility': 'Civilité',
            'phone': 'Téléphone',
            'first_name': 'Prénoms',
            'last_name': 'Nom',
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville de résidence',
            'address': 'Adresse',
            'martital_status': 'Situation matrimonial',
        }
        widgets = {
            'user': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'contract': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'bio': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
        }


class PartnerEditForm(PartnerCreateForm):
    class Meta:
        model = Driver
        fields = ('__all__')
        exclude = ('user',)
        labels = {
            'contract': 'Contrat',
            'nationality': 'Nationalité',
            'civility': 'Civilité',
            'phone': 'Téléphone',
            'first_name': 'Prénoms',
            'last_name': 'Nom',
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville de residence',
            'address': 'Adresse',
            'bio': 'Biographie',
            'martital_status': 'Situation matrimonial',
        }
        widgets = {
            'contract': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'bio': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
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
            'partner': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'issue_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'expiry_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'issuing_country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'is_vaid': forms.BooleanField(),
        }


class DriverCreateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('__all__')
        exclude = ('user', 'bio',)
        labels = {
            'nationality': 'Nationalité',
            'civility': 'Civilité',
            'first_name': 'Prénoms',
            'last_name': 'Nom',
            'phone': 'Téléphone',
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville',
            'address': 'Adresse',
            'martital_status': 'Situation matrimonial',
        }
        widgets = {
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
        }


class DriverEditForm(DriverCreateForm):
    class Meta:
        model = Driver
        fields = ('__all__')
        exclude = ('user',)
        labels = {
            'nationality': 'Nationalité',
            'civility': 'Civilité',
            'phone': 'Téléphone',
            'first_name': 'Prénoms',
            'last_name': 'Nom',
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville',
            'address': 'Adresse',
            'bio': 'Biographie',
            'martital_status': 'Situation matrimonial',
        }
        widgets = {
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'bio': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
        }


class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ('__all__')
        exclude = ('author',)
        labels = {
            'title': 'Titre',
            'driver': 'Conducteur',
            'vehicle': 'Véhicule',
            'repairability': 'Réparabilité',
            'place': 'Emplacement',
            'is_solved': 'Résolu',
            'severity': 'Type de cas',
            'date': "Date de l'incident",
            'time': "Heure de l'incident",
        }
        widgets = {
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'repairability': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'place': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'description': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'severity': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            # 'is_solved': forms.BooleanField(),
        }


class DocTypeForm(forms.ModelForm):

    class Meta:
        model = DocumentType
        fields = ('__all__')
        labels = {
            'name': 'Nom',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'description': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-xl bg-gray-200 w-full"}),
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
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'issue_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'expiry_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'issuing_country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'is_vaid': forms.BooleanField(),
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('__all__')
        exclude = ('date_added',)
        labels = {
            'owner': 'Propriétaire',
            'driver': 'Conducteur',
            'serial_number': 'Numéro de série (VIN)',
            'make': 'Marque',
            'model': 'Modèle',
            'plate_number': 'Immatriculation',
            'state': 'Etat',
            'year': 'Année de fabrication',
            'country': "Pays d'origine",
            'color': 'Couleur',
            'supplier': 'Fournisseurs',
            'management': 'Mode',
            'cost': 'Cout',
            'driver_count': 'Nombre de conducteurs',
            'first_driver': 'Premier conducteur',
            'second_driver': 'Deuxieme conducteur',
            'third_driver': 'Troisieme conducteur',
            'is_active': 'Actif',
        }
        widgets = {
            'owner': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'serial_number': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'make': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'model': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'plate_number': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'state': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'year': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'color': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'supplier': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'management': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'transmission': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'cost': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'driver_count': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'first_driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'second_driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'third_driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
        }


class VehicleDocumentForm(forms.ModelForm):

    class Meta:
        model = VehicleDocument
        fields = ('__all__')
        exclude = ('date_posted',)
        labels = {
            'vehicle': 'Véhicule',
            'type': 'Type de document',
            'issue_date': 'Délivré le',
            'expiry_date': 'Expire le',
            'issuing_country': 'Pays de délivrance',
            'is_valid': 'Validé',
        }
        widgets = {
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'issue_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'expiry_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'issuing_country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-gray-200 w-full"}),
            'is_vaid': forms.BooleanField(),
        }
