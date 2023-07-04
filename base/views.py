from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Min, Max

from accounts.models import Role
from finances.models import *


from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.


@login_required(login_url='login')
def home(req):
    user = req.user
    drivers = Driver.objects.all().count()
    partners = Partner.objects.all().count()
    vehicles = Vehicle.objects.all().count()
    incidents = Incident.objects.all().count()
    d_docs = DriverDocument.objects.all().count()
    p_docs = PartnerDocument.objects.all().count()
    v_docs = VehicleDocument.objects.all().count()

    context = {
        "home_page": "active",
        'title': 'home',
        'drivers': drivers,
        'partners': partners,
        'vehicles': vehicles,
        'incidents': incidents,
        'd_docs': d_docs,
        'p_docs': p_docs,
        'v_docs': v_docs,

    }
    return render(req, 'base/index.html', context)


# --------------------------------------------------------------------drivers CRUD--------------------------------------------------------

@login_required(login_url='login')
def drivers(req):
    user = req.user
    is_driver = False
    driver_check = Driver.objects.filter(user=user)
    if driver_check:
        is_driver = True
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    drivers = Driver.objects.filter(
        Q(city__icontains=query)
        | Q(address__icontains=query)
        | Q(first_name__icontains=query)
        | Q(last_name__icontains=query)
    )
    ordering = ['date_joined']

    context = {
        "drivers_page": "active",
        'title': 'drivers',
        'drivers': drivers,
        'is_driver': is_driver,
        'ordering': ordering,
    }
    return render(req, 'base/drivers.html', context)


@login_required(login_url='login')
def driver(req, pk):
    user = req.user
    curr_driver = Driver.objects.get(id=pk)
    documents = DriverDocument.objects.filter(driver=curr_driver)
    expenses = DriverExpense.objects.filter(driver=curr_driver)
    payouts = Payout.objects.filter(driver=curr_driver)
    payments = Payment.objects.filter(driver=curr_driver)
    incidents = Incident.objects.filter(driver=curr_driver)
    context = {
        "driver_page": "active",
        'title': 'driver',
        'curr_driver': curr_driver,
        'documents': documents,
        'expenses': expenses,
        'payments': payments,
        'payouts': payouts,
        'incidents': incidents,

    }
    return render(req, 'base/driver.html', context)


@login_required(login_url='login')
def create_driver(req):
    user = req.user
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DriverCreateForm()
    if req.method == 'POST':
        form = DriverCreateForm(req.POST)
        form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect('drivers')
    context = {
        "create_driver_page": "active", "title": 'create_driver', "user": user, "form": form}
    return render(req, 'base/driver.html', context)


@login_required(login_url='login')
def edit_driver(req, pk):
    user = req.user
    curr_driver = Driver.objects.get(id=pk)
    if curr_driver.user != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DriverEditForm(instance=curr_driver)
    if req.method == 'POST':
        form = DriverEditForm(req.POST, instance=curr_driver)
        if form.is_valid():
            form.save()
            return redirect('drivers')
    context = {
        "edit_driver_page": "active", "title": 'edit_driver', "user": user, "form": form, "curr_driver": curr_driver}
    return render(req, 'base/driver.html', context)


@login_required(login_url='login')
def delete_driver(req, pk):
    obj = Driver.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
# --------------------------------------------------------------------partners CRUD--------------------------------------------------------


@login_required(login_url='login')
def partners(req):
    user = req.user
    is_partner = False
    partner_check = Partner.objects.filter(user=user)
    if partner_check:
        is_partner = True
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    partners = Partner.objects.filter(
        Q(city__icontains=query)
        | Q(address__icontains=query)
        | Q(user__first_name__icontains=query)
        | Q(user__last_name__icontains=query)
    )
    ordering = ['date_joined']

    context = {
        "partners_page": "active",
        'title': 'partners',
        'partners': partners,
        'is_partner': is_partner,
        'ordering': ordering,
    }
    return render(req, 'base/partners.html', context)


@login_required(login_url='login')
def partner(req, pk):
    user = req.user
    curr_partner = Partner.objects.get(id=pk)
    documents = PartnerDocument.objects.filter(partner=curr_partner)
    vehicles = Vehicle.objects.filter(owner=curr_partner.user)
    payments = Payment.objects.filter(
        vehicle__in=Vehicle.objects.filter(owner=curr_partner.user))

    # for obj in vehicles:
    #     rev = Payment.objects.filter(vehicle=obj)
    #     payments.append(rev)

    # payments = payments

    print('Partner page', payments)
    context = {
        "partner_page": "active",
        'title': 'partner',
        'curr_partner': curr_partner,
        'documents': documents,
        'vehicles': vehicles,
        'payments': payments,

    }
    return render(req, 'base/partner.html', context)


@login_required(login_url='login')
def create_partner(req):
    user = req.user
    if user.role.sec_level < 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PartnerCreateForm()
    if req.method == 'POST':
        form = PartnerCreateForm(req.POST)
        form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect('partners')
    context = {
        "create_partner_page": "active", "title": 'create_partner', "user": user, "form": form}
    return render(req, 'base/partner.html', context)


@login_required(login_url='login')
def edit_partner(req, pk):
    user = req.user
    curr_partner = Partner.objects.get(id=pk)
    if curr_partner.user != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PartnerEditForm(instance=curr_partner)
    if req.method == 'POST':
        form = PartnerEditForm(req.POST, instance=curr_partner)
        if form.is_valid():
            form.save()
            return redirect('partners')
    context = {
        "edit_partner_page": "active", "title": 'edit_partner', "user": user, "form": form, "curr_partner": curr_partner}
    return render(req, 'base/partner.html', context)


@login_required(login_url='login')
def delete_partner(req, pk):
    obj = Partner.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
# --------------------------------------------------------------------vehicles CRUD--------------------------------------------------------


@login_required(login_url='login')
def vehicles(req):
    user = req.user
    has_vehicle = False
    vehicle_check = Vehicle.objects.filter(owner=user)
    if vehicle_check:
        has_vehicle = True
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    vehicles = Vehicle.objects.filter(
        Q(model__icontains=query)
        | Q(make__icontains=query)
        | Q(plate_number__icontains=query)
        | Q(transmission__icontains=query)
        | Q(owner__first_name__icontains=query)
        | Q(owner__last_name__icontains=query)
    )
    ordering = ['date_joined']

    context = {
        "vehicles_page": "active",
        'title': 'vehicles',
        'vehicles': vehicles,
        'has_vehicle': has_vehicle,
        'ordering': ordering,
    }
    return render(req, 'base/vehicles.html', context)


@login_required(login_url='login')
def vehicle(req, pk):
    user = req.user
    curr_vehicle = Vehicle.objects.get(plate_number=pk)
    docs = VehicleDocument.objects.filter(vehicle=curr_vehicle)
    payments = Payment.objects.filter(vehicle=curr_vehicle)
    expenses = VehicleExpense.objects.filter(vehicle=curr_vehicle)
    incidents = Incident.objects.filter(vehicle=curr_vehicle)
    context = {
        "vehicle_page": "active",
        'title': 'vehicle',
        'curr_vehicle': curr_vehicle,
        'docs': docs,
        'payments': payments,
        'expenses': expenses,
        'incidents': incidents,

    }
    return render(req, 'base/vehicle.html', context)


@login_required(login_url='login')
def create_vehicle(req):
    user = req.user
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VehicleForm()
    if req.method == 'POST':
        form = VehicleForm(req.POST)
        form.instance.owner = user
        if form.is_valid():
            form.save()
            return redirect('vehicles')
    context = {
        "create_vehicle_page": "active", "title": 'create_vehicle', "user": user, "form": form}
    return render(req, 'base/vehicle.html', context)


@login_required(login_url='login')
def edit_vehicle(req, pk):
    user = req.user
    curr_vehicle = Vehicle.objects.get(plate_number=pk)
    if curr_vehicle.owner != user:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VehicleForm(instance=curr_vehicle)
    if req.method == 'POST':
        form = VehicleForm(req.POST, instance=curr_vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicles')
    context = {
        "edit_vehicle_page": "active", "title": 'edit_vehicle', "user": user, "form": form, "curr_vehicle": curr_vehicle}
    return render(req, 'base/vehicle.html', context)


@login_required(login_url='login')
def delete_vehicle(req, pk):
    obj = Vehicle.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
# -------------------------------------------------------------------- documents CRUD --------------------------------------------------------


@login_required(login_url='login')
def documents(req):
    user = req.user
    d_docs = DriverDocument.objects.all()
    p_docs = PartnerDocument.objects.all()
    v_docs = VehicleDocument.objects.all()
    ordering = ['date_posted']

    context = {
        "documents_page": "active",
        'title': 'documents',
        'd_docs': d_docs,
        'p_docs': p_docs,
        'v_docs': v_docs,
        'ordering': ordering,
    }
    return render(req, 'base/documents/index.html', context)


# -------------------------------- driver documents ------------------------------------

@login_required(login_url='login')
def driver_docs(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    documents = DriverDocument.objects.filter(
        Q(driver__first_name__icontains=query)
        | Q(driver__last_name__icontains=query)
        | Q(type__name__icontains=query)
        | Q(issue_date__icontains=query)
        | Q(expiry_date__icontains=query)
    )
    ordering = ['date_posted']

    context = {
        "driver_documents_page": "active",
        'title': 'driver documents',
        'documents': documents,
        'ordering': ordering,
    }
    return render(req, 'base/documents/driver_docs.html', context)


@login_required(login_url='login')
def driver_doc(req, pk):
    user = req.user
    curr_doc = DriverDocument.objects.get(id=pk)
    rel_documents = DriverDocument.objects.filter(
        driver=curr_doc.driver).exclude(id=pk)
    context = {
        "document_page": "active",
        'title': 'driver document',
        'curr_doc': curr_doc,
        'rel_documents': rel_documents,

    }
    return render(req, 'base/documents/driver_doc.html', context)


@login_required(login_url='login')
def create_ddoc(req):
    user = req.user
    # if user.role.sec_level == 2:
    #     return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DriverDocumentForm()
    if req.method == 'POST':
        form = DriverDocumentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('documents')

    context = {
        "create_document_page": "active",
        "title": 'create driver document',
        "form": form,
    }
    return render(req, 'base/documents/driver_doc.html', context)


@login_required(login_url='login')
def edit_ddoc(req, pk):
    user = req.user
    curr_doc = DriverDocument.objects.get(id=pk)
    if curr_doc.driver != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DriverDocumentForm(instance=curr_doc)
    if req.method == 'POST':
        form = DriverDocumentForm(req.POST, instance=curr_doc)
        if form.is_valid():
            form.save()
            return redirect('documents')

    context = {
        "edit_document_page": "active",
        "title": 'edit_driver_document',
        "form": form,
        "curr_doc": curr_doc}
    return render(req, 'base/documents/driver_doc.html', context)


@login_required(login_url='login')
def delete_ddoc(req, pk):
    obj = DriverDocument.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# -------------------------------- partner documents ------------------------------------

@login_required(login_url='login')
def partner_docs(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    documents = PartnerDocument.objects.filter(
        Q(partner__first_name__icontains=query)
        | Q(partner__last_name__icontains=query)
        | Q(type__name__icontains=query)
        | Q(issue_date__icontains=query)
        | Q(expiry_date__icontains=query)
    )
    ordering = ['date_posted']

    context = {
        "partner_documents_page": "active",
        'title': 'partner documents',
        'documents': documents,
        'ordering': ordering,
    }
    return render(req, 'base/documents/partner_docs.html', context)


@login_required(login_url='login')
def partner_doc(req, pk):
    user = req.user
    curr_doc = PartnerDocument.objects.get(id=pk)
    rel_documents = PartnerDocument.objects.filter(
        partner=curr_doc.partner).exclude(id=pk)
    context = {
        "document_page": "active",
        'title': 'driver_document',
        'curr_doc': curr_doc,
        'rel_documents': rel_documents,

    }
    return render(req, 'base/documents/partner_doc.html', context)


@login_required(login_url='login')
def create_pdoc(req):
    user = req.user
    # if user.role.sec_level == 2:
    #     return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PartnerDocumentForm()
    if req.method == 'POST':
        form = PartnerDocumentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('documents')

    context = {
        "create_document_page": "active",
        "title": 'create_driver_document',
        "form": form,
    }
    return render(req, 'base/documents/partner_doc.html', context)


@login_required(login_url='login')
def edit_pdoc(req, pk):
    user = req.user
    curr_doc = DriverDocument.objects.get(id=pk)
    if curr_doc.driver != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PartnerDocument(instance=curr_doc)
    if req.method == 'POST':
        form = PartnerDocumentForm(req.POST, instance=curr_doc)
        if form.is_valid():
            form.save()
            return redirect('documents')

    context = {
        "edit_document_page": "active",
        "title": 'edit_driver_document',
        "form": form,
        "curr_doc": curr_doc,
    }
    return render(req, 'base/documents/partner_doc.html', context)


@login_required(login_url='login')
def delete_pdoc(req, pk):
    obj = PartnerDocument.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# -------------------------------- vehicle documents ------------------------------------


@login_required(login_url='login')
def vehicle_docs(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    documents = VehicleDocument.objects.filter(
        Q(type__name__icontains=query)
        | Q(issue_date__icontains=query)
        | Q(expiry_date__icontains=query)
    )
    ordering = ['date_posted']

    context = {
        "vehicle_documents_page": "active",
        'title': 'vehicle documents',
        'documents': documents,
        'ordering': ordering,
    }
    return render(req, 'base/documents/vehicle_docs.html', context)


login_required(login_url='login')


def create_vdoc(req):
    user = req.user
    # if user.role.sec_level < 2:
    #     return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VehicleDocumentForm()
    if req.method == 'POST':
        form = VehicleDocumentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('documents')

    context = {
        "create_document_page": "active",
        "title": 'create_vehicle_document',
        "form": form,
    }
    return render(req, 'base/documents/vehicle_doc.html', context)


@login_required(login_url='login')
def vehicle_doc(req, pk):
    user = req.user
    curr_doc = VehicleDocument.objects.get(id=pk)
    rel_documents = VehicleDocument.objects.filter(
        vehicle=curr_doc.vehicle).exclude(id=pk)
    context = {
        "document_page": "active",
        'title': 'vehicle_document',
        'curr_doc': curr_doc,
        'rel_documents': rel_documents,

    }
    return render(req, 'base/documents/vehicle_doc.html', context)


@login_required(login_url='login')
def edit_vdoc(req, pk):
    user = req.user
    curr_doc = VehicleDocument.objects.get(id=pk)
    if curr_doc.vehicle.owner != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VehicleDocumentForm(instance=curr_doc)
    if req.method == 'POST':
        form = VehicleDocumentForm(req.POST, instance=curr_doc)
        if form.is_valid():
            form.save()
            return redirect('documents')
    context = {
        "edit_document_page": "active",
        "title": 'edit_vehicle_document',
        "form": form,
        "curr_doc": curr_doc}
    return render(req, 'base/documents/vehicle_doc.html', context)


@login_required(login_url='login')
def delete_vdoc(req, pk):
    obj = VehicleDocument.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# -------------------------------------------------------------------- incidents CRUD --------------------------------------------------------


@login_required(login_url='login')
def incidents(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    if user.role.sec_level < 3:
        incidents = Incident.objects.filter(
            Q(vehicle__plate_number__icontains=query)
            | Q(vehicle__model__icontains=query)
            | Q(vehicle__make__icontains=query), driver=user.driver
        ).order_by('date_posted')
    else:
        incidents = Incident.objects.filter(
            Q(vehicle__plate_number__icontains=query)
            | Q(vehicle__model__icontains=query)
            | Q(vehicle__make__icontains=query)
            | Q(driver__first_name__icontains=query)
            | Q(driver__first_name__icontains=query)
        ).order_by('date_posted')

    context = {
        "incidents_page": "active",
        'title': 'incidents',
        'incidents': incidents,
    }
    return render(req, 'base/incidents.html', context)


@login_required(login_url='login')
def incident(req, pk):
    user = req.user
    curr_incident = Incident.objects.get(id=pk)
    context = {
        "incident_page": "active",
        'title': 'incident',
        'curr_incident': curr_incident,

    }
    return render(req, 'base/incident.html', context)


@login_required(login_url='login')
def create_incident(req):
    user = req.user
    # if user.role.sec_level < 2:
    #     return redirect(req.META.get('HTTP_REFERER', '/'))

    form = IncidentForm()
    if req.method == 'POST':
        form = IncidentForm(req.POST)
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('incidents')
    context = {
        "create_incident_page": "active",
        "title": 'create_incident',
        "form": form
    }
    return render(req, 'base/incident.html', context)


@login_required(login_url='login')
def edit_incident(req, pk):
    user = req.user
    curr_incident = Incident.objects.get(id=pk)
    if curr_incident.author != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = IncidentForm(instance=curr_incident)
    if req.method == 'POST':
        form = IncidentForm(req.POST, instance=curr_incident)
        if form.is_valid():
            form.save()
            return redirect('incidents')
    context = {
        "edit_incident_page": "active",
        "title": 'edit_incident',
        "form": form,
        "curr_incident": curr_incident
    }
    return render(req, 'base/incident.html', context)


@login_required(login_url='login')
def delete_incident(req, pk):
    obj = Incident.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def parameters(req):
    user = req.user
    doc_types = DocumentType.objects.all()
    roles = Role.objects.all()
    context = {
        "parameters_page": "active",
        "title": 'parameters',
        "doc_types": doc_types,
        "roles": roles
    }
    return render(req, 'parameters/index.html', context)
