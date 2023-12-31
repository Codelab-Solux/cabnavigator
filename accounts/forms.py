from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs) -> None:
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"
        self.fields['password2'].widget.attrs['class'] = "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"
        self.fields['password1'].label = "Mot de pass"
        self.fields['password2'].label = "Confirmez votre mot de pass"

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'role'
        )
        labels = {'username': 'Nom d’utilisateur', 'email': 'Email',
                  'first_name': 'Prenoms', 'last_name': 'Nom', 'phone': 'Telephone', 'role': 'Type de compte'
                  }
        widgets = {
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'role': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs) -> None:
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = "mb-2 px-4 py-2 rounded-md  border-gray-200 focus:border-black w-full"
        self.fields['password2'].widget.attrs['class'] = "mb-2 px-4 py-2 rounded-md  border-gray-200 focus:border-black w-full"
        self.fields['password1'].label = "Mot de pass"
        self.fields['password2'].label = "Confirmez votre mot de pass"

    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2',
        )
        labels = {'username': 'Nom d’utilisateur', 'email': 'Email',
                  'first_name': 'Prenoms', 'last_name': 'Nom', 'phone': 'Telephone', 'role': 'Type de compte'
                  }
        widgets = {
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            # 'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            # 'role': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')
        exclude = ('groups', 'user_permissions',
                   'password', 'last_login', 'is_staff', 'is_superuser', 'is_active')
        labels = {'username': 'Nom d’utilisateur', 'email': 'Email',
                  'first_name': 'Prenoms', 'last_name': 'Nom', 'phone': 'Telephone', 'role': 'Type de compte'
                  }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'role': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class AdminEditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')
        exclude = ('groups', 'user_permissions',
                   'password', 'last_login', 'is_staff', 'is_superuser')
        labels = {'username': 'Nom d’utilisateur', 'email': 'Email',
                  'first_name': 'Prenoms', 'last_name': 'Nom', 'phone': 'Telephone', 'role': 'Type de compte'
                  }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'role': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }


class RoleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
            'sec_level': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-black w-full"}),
        }
