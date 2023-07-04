from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from django_countries.fields import CountryField


class Contract(models.Model):
    title = models.CharField(max_length=255, default='')
    commission = models.IntegerField(null=False, blank=True, default='0')
    terms = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} ({self.commission} %)'

    def get_absolute_url(self):
        return reverse('contract', kwargs={'pk': self.pk})


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
    contract = models.ForeignKey(
        Contract, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
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
    image = models.ImageField(upload_to='partners', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse('partner', kwargs={'pk': self.pk})


class Driver(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    civility = models.CharField(max_length=50, default='', choices=civ_titles)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
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
    image = models.ImageField(upload_to='drivers', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('driver', kwargs={'pk': self.pk})


class DocumentType(models.Model):
    name = models.CharField(max_length=255, default='',)
    description = models.TextField(blank=True, null=True, default='',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('document_type', kwargs={'pk': self.pk})


class DriverDocument(models.Model):
    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(blank=True,)
    expiry_date = models.DateTimeField(blank=True,)
    issuing_country = CountryField(
        blank_label="", blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='driver_docs', blank=True, null=True)

    def __str__(self):
        return f'{self.driver.first_name}({self.type.name})'

    def get_absolute_url(self):
        return reverse('driver_doc', kwargs={'pk': self.pk})


class PartnerDocument(models.Model):
    partner = models.ForeignKey(
        Partner, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    issuing_country = CountryField(
        blank_label="", blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='partner_docs', blank=True, null=True)

    def __str__(self):
        return f'{self.driver.user.first_name}({self.type.name})'

    def get_absolute_url(self):
        return reverse('partner_doc', kwargs={'pk': self.pk})


transmission_types = (
    ('Manuelle', 'Manuelle'),
    ('Automatique', "Automatique"),
)

usage_states = (
    ('Neuf', 'Neuf'),
    ('Usagé ', "Usagé "),
)

mgt_modes = (
    ('Propriété personnelle', 'Propriété personnelle'),
    ('Mandat de gestion', "Mandat de gestion"),
)


class Vehicle(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cost = models.IntegerField(default='0',)
    serial_number = models.CharField(max_length=255, default='', unique=True)
    make = models.CharField(max_length=255, default='',)
    model = models.CharField(max_length=255, default='',)
    plate_number = models.CharField(
        max_length=255, primary_key=True, unique=True)
    year = models.IntegerField(default='')
    country = CountryField(
        blank_label="", blank=True, null=True)
    transmission = models.CharField(
        max_length=50, default='', choices=transmission_types)
    state = models.CharField(
        max_length=50, default='', choices=usage_states)
    color = models.CharField(max_length=255, default='',)
    supplier = models.CharField(max_length=255, default='',)
    management = models.CharField(
        max_length=50, default='', choices=mgt_modes)
    date_added = models.DateTimeField(auto_now=True)
    driver_count = models.IntegerField(default='0',)
    first_driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='first_driver')
    second_driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='second_driver')
    third_driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='third_driver')
    image = models.ImageField(upload_to='vehicles', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.make

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
    date_posted = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='vehicle_docs', blank=True, null=True)

    def __str__(self):
        return f'{self.vehicle.make}{self.vehicle.plate_number}({self.type.name})'

    def get_absolute_url(self):
        return reverse('vehicle_doc', kwargs={'pk': self.pk})


severity_levels = (
    ('mineur', 'Mineur'),
    ('majeur', "Majeur"),
    ('fatal', "Fatal"),
)

repair_levels = (
    ('repairable', 'Reparable'),
    ('unrepairable', "Irreparable"),
)


class Incident(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    severity = models.CharField(max_length=50, blank=True,
                                null=True, choices=severity_levels, default='')
    repairability = models.CharField(max_length=50, blank=True,
                                     null=True, choices=repair_levels, default='')
    title = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=128)
    is_solved = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='incidents', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('incident', kwargs={'pk': self.pk})
