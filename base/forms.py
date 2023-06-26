
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class PartnerCreateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('__all__')
        exclude = ('user', 'bio',)
        labels = {
            'nationality': 'Nationalité',
            'civility': 'Civilité',
            'phone': 'Téléphone',
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville',
            'address': 'Adresse',
            'martital_status': 'Situation matrimonial',
        }
        widgets = {
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class PartnerEditForm(PartnerCreateForm):
    class Meta:
        model = Driver
        fields = ('__all__')
        exclude = ('user',)
        labels = {
            'nationality': 'Nationalité',
            'civility': 'Civilité',
            'phone': 'Téléphone',
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville',
            'address': 'Adresse',
            'bio': 'Biographie',
            'martital_status': 'Situation matrimonial',
        }
        widgets = {
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'bio': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class DriverCreateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('__all__')
        exclude = ('user', 'bio',)
        labels = {
            'nationality': 'Nationalité',
            'civility': 'Civilité',
            'phone': 'Téléphone',
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville',
            'address': 'Adresse',
            'martital_status': 'Situation matrimonial',
        }
        widgets = {
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
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
            'date_of_birth': 'Date de naissance',
            'place_of_birth': 'Lieu de naissance',
            'city': 'Ville',
            'address': 'Adresse',
            'bio': 'Biographie',
            'martital_status': 'Situation matrimonial',
        }
        widgets = {
            'nationality': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'martital_status': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'place_of_birth': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'city': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'bio': forms.Textarea(attrs={"rows": "6", 'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
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
            'is_solved': 'Résolu',
            'severity': 'Type de cas',
            'date': "Date de l'incident",
            'time': "Heure de l'incident",
        }
        widgets = {
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'description': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-xl bg-white w-full"}),
            'severity': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'time': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
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
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'description': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-xl bg-white w-full"}),
        }


class DriverDocumentForm(forms.ModelForm):

    class Meta:
        model = DriverDocument
        fields = ('__all__')
        exclude = ('user',)
        labels = {
            'driver': 'Conducteur',
            'type': 'Type de document',
            'issue_date': 'Délivré le',
            'expiry_date': 'Expire le',
            'issuing_country': 'Pays de délivrance',
            'is_valid': 'Validé',
        }
        widgets = {
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'issue_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'expiry_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'issuing_country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'is_vaid': forms.BooleanField(),
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('__all__')
        exclude = ('owner', 'date_added')
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
        }
        widgets = {
            'owner': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'driver': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'serial_number': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'make': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'model': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'plate_number': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'state': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'year': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'color': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'date_of_birth': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'supplier': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'management': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'transmission': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
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
            'vehicle': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'issue_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'expiry_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'issuing_country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'is_vaid': forms.BooleanField(),
        }
