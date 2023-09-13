from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from django_countries.fields import CountryField

from chats.models import ChatMessage


legal_statuses = (
    ('EURL', 'EURL'),
    ('SARL', 'SARL'),
    ('SARLU', 'SARLU'),
    ('SAS', 'SAS'),
    ('SA', "SA"),
)

incident_statuses = (
    ('open', 'Ouvert'),
    ('pending', 'En cours'),
    ('closed', 'Cloturé'),
)


class Company(models.Model):
    name = models.CharField(max_length=255, default='')
    reg_number = models.CharField(max_length=255, default='')
    fiscal_id = models.CharField(max_length=255, default='')
    legal_status = models.CharField(
        max_length=50, default='', choices=legal_statuses)
    social_capital = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    country = CountryField(blank_label="", blank=True, null=True)
    phone = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    logo = models.ImageField(upload_to='company/logos', blank=True, null=True)
    banner = models.ImageField(
        upload_to='company/banners', blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.reg_number}'

    def get_absolute_url(self):
        return reverse('company', kwargs={'pk': self.pk})


class IncidentType(models.Model):
    name = models.CharField(max_length=255, default='',)
    description = models.TextField(blank=True, null=True, default='',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('incident_type', kwargs={'pk': self.pk})


class DocumentType(models.Model):
    name = models.CharField(max_length=255, default='',)
    description = models.TextField(blank=True, null=True, default='',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('document_type', kwargs={'pk': self.pk})


civ_titles = (
    ('M.', 'M.'),
    ('Mme.', "Mme"),
    ('Mlle.', "Mlle"),
)

marital_statuses = (
    ('Célibataire', 'Célibataire'),
    ('Marié(e)', 'Marié(e)'),
    ('Divorcé(e)', 'Divorcé(e)'),
    ('Voeuf(ve)', "Voeuf(ve)"),
)


class Partner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    commission = models.IntegerField(null=False, blank=True, default='0')
    civility = models.CharField(max_length=50, default='', choices=civ_titles)
    first_name = models.CharField(
        max_length=255, default='', null=True, blank=True)
    last_name = models.CharField(
        max_length=255, default='', null=True, blank=True)
    martital_status = models.CharField(
        max_length=50, default='', choices=marital_statuses)
    nationality = CountryField(
        blank_label="", blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, default='',)
    city = models.CharField(max_length=255, default='',)
    phone = models.CharField(max_length=255, default='',)
    address = models.CharField(max_length=255, default='',)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='partners/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} - {self.user.email}'

    def get_absolute_url(self):
        return reverse('partner', kwargs={'pk': self.pk})


class PartnerDocument(models.Model):
    partner = models.ForeignKey(
        Partner, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    issuing_country = CountryField(
        blank_label="", blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='partner_docs/', blank=True, null=True)

    def __str__(self):
        return f'{self.driver.user.first_name}({self.type.name})'

    def get_absolute_url(self):
        return reverse('partner_doc', kwargs={'pk': self.pk})


class Driver(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # vehicle = models.ForeignKey(
    #     'Vehicle', on_delete=models.SET_NULL, null=True, blank=True)
    civility = models.CharField(max_length=50, default='', choices=civ_titles)
    martital_status = models.CharField(
        max_length=50, default='', choices=marital_statuses)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nationality = CountryField(
        blank_label="", blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(
        max_length=255, default='', blank=True, null=True)
    city = models.CharField(max_length=255, default='', blank=True, null=True)
    phone = models.CharField(max_length=255, default='',)
    address = models.CharField(
        max_length=255, default='', blank=True, null=True)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='drivers', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    # ------------------------------------------------
    score = models.IntegerField(null=False, blank=True, default='100')
    observation = models.CharField(
        max_length=1000, default='', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.user.email}'

    def get_absolute_url(self):
        return reverse('driver', kwargs={'pk': self.pk})


class DriverDocument(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True,
                               blank=True)
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(blank=True,)
    expiry_date = models.DateTimeField(blank=True,)
    issuing_country = CountryField(
        blank_label="", blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='driver_docs/', blank=True, null=True)

    def __str__(self):
        return f'{self.driver.first_name}({self.type.name})'

    def get_absolute_url(self):
        return reverse('driver_doc', kwargs={'pk': self.pk})


transmission_types = (
    ('Manuelle', 'Manuelle'),
    ('Automatique', "Automatique"),
)

usage_states = (
    ('Neuf', 'Neuf'),
    ('Usagé ', "Usagé "),
)


class Vehicle(models.Model):
    owner = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL,  null=True, blank=True)
    supplier = models.CharField(
        max_length=255, null=True, blank=True,)
    first_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True,
                                     blank=True, related_name='first_driver')
    second_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True,
                                      blank=True, related_name='second_driver')
    third_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True,
                                     blank=True, related_name='third_driver')
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    country = CountryField(blank_label="", blank=True, null=True)
    plate_number = models.CharField(
        max_length=255, primary_key=True, unique=True)
    serial_number = models.CharField(
        max_length=255, unique=True, null=True, blank=True)
    state = models.CharField(max_length=50,  choices=usage_states)
    transmission = models.CharField(max_length=50, choices=transmission_types)
    color = models.CharField(max_length=255, null=True, blank=True)
    cost = models.IntegerField(default='0')
    commission = models.IntegerField(default='10')
    image = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.make} - {self.model} [{self.plate_number}]'

    def get_absolute_url(self):
        return reverse('vehicle', kwargs={'pk': self.pk})


class VehicleDocument(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(blank=True,)
    expiry_date = models.DateTimeField(blank=True, null=True)
    issuing_country = CountryField(
        blank_label="", blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='vehicle_docs/', blank=True, null=True)

    def __str__(self):
        return f'{self.vehicle.plate_number}({self.type.name})'

    def get_absolute_url(self):
        return reverse('vehicle_doc', kwargs={'pk': self.pk})


repair_levels = (
    ('repairable', 'Reparable'),
    ('unrepairable', "Irreparable"),
)

mobility_status = (
    ('mobile', 'Mobilisé'),
    ('immobile', "Immobilisé"),
)


class Incident(models.Model):
    type = models.ForeignKey(
        IncidentType, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    repairability = models.CharField(max_length=50, blank=True,
                                     null=True, choices=repair_levels, default='')
    mobility = models.CharField(max_length=50, blank=True,
                                null=True, choices=mobility_status, default='')
    title = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=128)
    cost = models.IntegerField(null=True, blank=True, default=0)
    is_solved = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='incidents/', blank=True, null=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('incident', kwargs={'pk': self.pk})


class Tip(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    article = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='tips/images/', blank=True, null=True)
    video = models.FileField(upload_to='tips/videos/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tip', kwargs={'pk': self.pk})


class ChatNotification(models.Model):
    chat = models.ForeignKey(to=ChatMessage, on_delete=models.CASCADE)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Notification for < user: {self.user.username}>'

    def get_absolute_url(self):
        return reverse('chat_notification', kwargs={'pk': self.pk})
