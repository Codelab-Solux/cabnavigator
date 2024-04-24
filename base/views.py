from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Min, Max
from django.contrib import messages
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
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    query = req.GET.get('query') if req.GET.get('query') != None else ''
    drivers = Driver.objects.filter(
        Q(city__icontains=query)
        | Q(address__icontains=query)
        | Q(first_name__icontains=query)
        | Q(last_name__icontains=query)
    )
    ordering = ['date_joined']

    driver_count = Driver.objects.all().count()
    if driver_count > 0:
        activ_count = Driver.objects.filter(is_active=True).count()
        inactiv_count = Driver.objects.filter(is_active=False).count()
        activity_percent = activ_count * 100 / driver_count
    else:
        activ_count = 0
        inactiv_count = 0
        activity_percent = 0

    print(drivers)
    context = {
        "drivers_page": "active",
        'title': 'drivers',
        'drivers': drivers,
        'ordering': ordering,
        'driver_count': driver_count,
        'activ_count': activ_count,
        'inactiv_count': inactiv_count,
        'activity_percent': activity_percent,
    }
    return render(req, 'base/drivers.html', context)


@login_required(login_url='login')
def driver(req, pk):
    user = req.user
    curr_driver = Driver.objects.get(id=pk)
    if curr_driver.user != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    documents = DriverDocument.objects.filter(driver=curr_driver)
    expenses = DriverExpense.objects.filter(driver=curr_driver)
    payouts = Payout.objects.filter(driver=curr_driver)
    payments = Payment.objects.filter(driver=curr_driver)
    incidents = Incident.objects.filter(driver=curr_driver)
    context = {
        "drivers_page": "active",
        'title': 'driver details',
        'curr_driver': curr_driver,
        'documents': documents,
        'expenses': expenses,
        'payments': payments,
        'payouts': payouts,
        'incidents': incidents,

    }
    return render(req, 'base/driver.html', context)


@login_required(login_url='login')
def driver_activation(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            driver = Driver.objects.get(id=pk)
            if driver.is_active == False:
                Driver.objects.filter(id=pk).update(is_active=True)
            else:
                Driver.objects.filter(id=pk).update(is_active=False)
        except Driver.DoesNotExist:
            return HttpResponse('Driver not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def driver_profile(req):
    user = req.user
    curr_driver = Driver.objects.get(user=user)
    if not curr_driver:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    documents = DriverDocument.objects.filter(driver=curr_driver)
    expenses = DriverExpense.objects.filter(driver=curr_driver)
    payouts = Payout.objects.filter(driver=curr_driver)
    payments = Payment.objects.filter(driver=curr_driver)
    incidents = Incident.objects.filter(driver=curr_driver)
    context = {
        "drivers_page": "active",
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
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    else:
        form = DriverForm()
        if req.method == 'POST':
            form = DriverForm(req.POST, req.FILES)
            if form.is_valid():
                print('valid form')
                form.save()
                return redirect('drivers')
    context = {
        "drivers_page": "active",
        "title": 'create driver',
        "form": form
    }
    return render(req, 'base/driver.html', context)


@login_required(login_url='login')
def edit_driver(req, pk):
    user = req.user
    curr_driver = Driver.objects.get(id=pk)
    if curr_driver.user != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    else:
        form = DriverForm(instance=curr_driver)
        if req.method == 'POST':
            form = DriverForm(req.POST, req.FILES, instance=curr_driver)
            if form.is_valid():
                print('valid form')
                form.save()
                return redirect('drivers')

    context = {
        "drivers_page": "active",
        "title": 'edit driver',
        "form": form,
        "curr_driver": curr_driver,
    }
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
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    query = req.GET.get('query') if req.GET.get('query') != None else ''
    partners = Partner.objects.filter(
        Q(city__icontains=query)
        | Q(address__icontains=query)
        | Q(user__first_name__icontains=query)
        | Q(user__last_name__icontains=query)
    )
    ordering = ['date_joined']

    partner_count = Partner.objects.all().count()
    if partner_count > 0:
        activ_count = Partner.objects.filter(is_active=True).count()
        inactiv_count = Partner.objects.filter(is_active=False).count()
        activity_percent = activ_count * 100 / partner_count
    else:
        activ_count = 0
        inactiv_count = 0
        activity_percent = 0

    context = {
        "partners_page": "active",
        'title': 'partners',
        'partners': partners,
        'ordering': ordering,
        'partner_count': partner_count,
        'activ_count': activ_count,
        'inactiv_count': inactiv_count,
        'activity_percent': activity_percent,
    }
    return render(req, 'base/partners.html', context)


@login_required(login_url='login')
def partner(req, pk):
    user = req.user
    curr_partner = Partner.objects.get(id=pk)
    if curr_partner.user != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    documents = PartnerDocument.objects.filter(partner=curr_partner)
    vehicles = Vehicle.objects.filter(owner=curr_partner.user)
    payments = Payment.objects.filter(
        vehicle__in=Vehicle.objects.filter(owner=curr_partner.user))
    revenues = Revenue.objects.filter(partner=curr_partner)
    total_revenu = Payment.objects.filter(
        vehicle__in=Vehicle.objects.filter(owner=curr_partner.user)).aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_expenses = VehicleExpense.objects.filter(
        vehicle__in=Vehicle.objects.filter(owner=curr_partner.user)).aggregate(Sum('amount'))[
        'amount__sum'] or 0
    net_revenu = total_revenu - total_expenses
    commission = (total_revenu - total_expenses) * \
        curr_partner.commission/100
    total_net = net_revenu - commission

    print('total revenu : ', total_revenu,
          'total_expenses :', total_expenses,
          'net_revenu :', net_revenu,
          'total_net :', total_net,
          'commission :', commission,
          )
    context = {
        "partners_page": "active",
        'title': 'partner details',
        'curr_partner': curr_partner,
        'documents': documents,
        'vehicles': vehicles,
        'payments': payments,
        'revenues': revenues,
        'total_revenu': total_revenu,
        'total_expenses': total_expenses,
        'net_revenu': net_revenu,
        'commission': commission,
        'total_net': total_net,

    }
    return render(req, 'base/partner.html', context)


@login_required(login_url='login')
def partner_activation(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            partner = Partner.objects.get(id=pk)
            if partner.is_active == False:
                Partner.objects.filter(id=pk).update(is_active=True)
            else:
                Partner.objects.filter(id=pk).update(is_active=False)
        except Partner.DoesNotExist:
            return HttpResponse('Partner not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def partner_profile(req):
    user = req.user
    curr_partner = Partner.objects.get(user=user)
    if not curr_partner:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    documents = PartnerDocument.objects.filter(partner=curr_partner)
    vehicles = Vehicle.objects.filter(owner=curr_partner.user)
    payments = Payment.objects.filter(
        vehicle__in=Vehicle.objects.filter(owner=curr_partner.user))
    revenues = Revenue.objects.filter(partner=curr_partner)
    total_revenu = Payment.objects.filter(
        vehicle__in=Vehicle.objects.filter(owner=curr_partner.user)).aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_expenses = VehicleExpense.objects.filter(
        vehicle__in=Vehicle.objects.filter(owner=curr_partner.user)).aggregate(Sum('amount'))[
        'amount__sum'] or 0
    net_revenu = total_revenu - total_expenses
    commission = (total_revenu - total_expenses) * \
        curr_partner.commission/100
    total_net = net_revenu - commission

    print('total revenu : ', total_revenu,
          'total_expenses :', total_expenses,
          'net_revenu :', net_revenu,
          'total_net :', total_net,
          'commission :', commission,
          )
    context = {
        "partners_page": "active",
        'title': 'partner details',
        'curr_partner': curr_partner,
        'documents': documents,
        'vehicles': vehicles,
        'payments': payments,
        'revenues': revenues,
        'total_revenu': total_revenu,
        'total_expenses': total_expenses,
        'net_revenu': net_revenu,
        'commission': commission,
        'total_net': total_net,

    }
    return render(req, 'base/partner.html', context)


@login_required(login_url='login')
def create_partner(req):
    user = req.user
    if user.role.sec_level < 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    elif user.role.sec_level == 2:
        partner_check = Partner.objects.get(user=user)
        if not partner_check:
            return redirect(req.META.get('HTTP_REFERER', '/'))

        form = PartnerForm()
        if req.method == 'POST':
            form = PartnerForm(req.POST, req.FILES)
            form.instance.user = user
            if form.is_valid():
                print('valid')
                form.save()
                return redirect('partners')
    else:
        form = PartnerForm()
        if req.method == 'POST':
            form = PartnerForm(req.POST, req.FILES)
            if form.is_valid():
                print('valid')
                form.save()
                return redirect('partners')
    context = {
        "partners_page": "active",
        "title": 'create partner',
        "form": form
    }
    return render(req, 'base/partner.html', context)


@login_required(login_url='login')
def edit_partner(req, pk):
    user = req.user
    curr_partner = Partner.objects.get(id=pk)
    if curr_partner.user != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    else:
        form = PartnerForm(instance=curr_partner)
        if req.method == 'POST':
            form = PartnerForm(req.POST, req.FILES, instance=curr_partner)
            if form.is_valid():
                print('valid form')
                form.save()
                return redirect('partners')
    context = {
        "partners_page": "active",
        "title": 'edit partner',
        "form": form,
        "curr_partner": curr_partner
    }
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
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    if user.role.sec_level < 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 2:
        vehicles = Vehicle.objects.filter(
            Q(model__icontains=query)
            | Q(make__icontains=query)
            | Q(plate_number__icontains=query)
            | Q(transmission__icontains=query), owner=user
        )
        company_vehicles = 0,
        owned_vehicles = 0,
        comp_activ_count = 0,
        owned_activ_count = 0,
        comp_inactiv_count = 0,
        owned_inactiv_count = 0,
        vehicle_count = vehicles.count()
        if vehicle_count > 0:
            activ_count = vehicles.filter(is_active=True).count()
            inactiv_count = vehicles.filter(is_active=False).count()
            activity_percent = activ_count * 100 / vehicle_count
        else:
            activ_count = 0
            inactiv_count = 0
            activity_percent = 0
    else:
        vehicles = Vehicle.objects.filter(
            Q(model__icontains=query)
            | Q(make__icontains=query)
            | Q(plate_number__icontains=query)
            | Q(transmission__icontains=query)
            | Q(owner__first_name__icontains=query)
            | Q(owner__last_name__icontains=query)
        )
        vehicle_count = vehicles.count()
        company_vehicles = vehicles.filter(owner=None).count()
        owned_vehicles = vehicle_count - company_vehicles
        if vehicle_count > 0:
            activ_count = vehicles.filter(is_active=True).count()
            comp_activ_count = vehicles.filter(
                owner=None, is_active=True).count()
            owned_activ_count = activ_count - comp_activ_count
# -----------------------------------------
            inactiv_count = vehicles.filter(is_active=False).count()
            comp_inactiv_count = vehicles.filter(
                owner=None, is_active=False).count()
            owned_inactiv_count = inactiv_count - comp_inactiv_count
# -----------------------------------------

            activity_percent = activ_count * 100 / vehicle_count
        else:
            activ_count = 0
            inactiv_count = 0
            activity_percent = 0

    ordering = ['date_added']

    context = {
        "vehicles_page": "active",
        'title': 'vehicles',
        'vehicles': vehicles,
        'ordering': ordering,
        'vehicle_count': vehicle_count,
        'activ_count': activ_count,
        'inactiv_count': inactiv_count,
        'activity_percent': activity_percent,
        'company_vehicles': company_vehicles,
        'owned_vehicles': owned_vehicles,
        'comp_activ_count': comp_activ_count,
        'owned_activ_count': owned_activ_count,
        'comp_inactiv_count': comp_inactiv_count,
        'owned_inactiv_count': owned_inactiv_count,
    }
    return render(req, 'base/vehicles.html', context)


@login_required(login_url='login')
def vehicle(req, pk):
    user = req.user
    if user.role.sec_level == 1:
        curr_driver = Driver.objects.get(user=user)
        if not curr_driver:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        curr_vehicle = Vehicle.objects.get(
            Q(first_driver=curr_driver) |
            Q(second_driver=curr_driver) |
            Q(third_driver=curr_driver), plate_number=pk)
        if not curr_vehicle:
            return redirect(req.META.get('HTTP_REFERER', '/'))

    elif user.role.sec_level == 2:
        curr_vehicle = Vehicle.objects.get(plate_number=pk, owner=user)
        if not curr_vehicle:
            return redirect(req.META.get('HTTP_REFERER', '/'))
    else:
        curr_vehicle = Vehicle.objects.get(plate_number=pk)
        if not curr_vehicle:
            return redirect(req.META.get('HTTP_REFERER', '/'))

    docs = VehicleDocument.objects.filter(vehicle=curr_vehicle)
    payments = Payment.objects.filter(vehicle=curr_vehicle)
    expenses = VehicleExpense.objects.filter(vehicle=curr_vehicle)
    incidents = Incident.objects.filter(vehicle=curr_vehicle)
    total_revenu = Payment.objects.filter(vehicle=curr_vehicle).aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_expenses = VehicleExpense.objects.filter(vehicle=curr_vehicle).aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_net = total_revenu - total_expenses
    total_commission = total_revenu/curr_vehicle.commission
    context = {
        "vehicles_page": "active",
        'title': 'vehicle details',
        'curr_vehicle': curr_vehicle,
        'docs': docs,
        'payments': payments,
        'expenses': expenses,
        'incidents': incidents,
        'total_revenu': total_revenu/100,
        'total_expenses': total_expenses/100,
        'total_commission': total_commission/100,
        'total_net': total_net,

    }
    return render(req, 'base/vehicle.html', context)


@login_required(login_url='login')
def my_vehicle(req):
    user = req.user
    if user.role.sec_level != 1:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    else:
        curr_driver = Driver.objects.get(user=user)
        if not curr_driver:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        curr_vehicle = Vehicle.objects.get(
            Q(first_driver=curr_driver) |
            Q(second_driver=curr_driver) |
            Q(third_driver=curr_driver))
        if not curr_vehicle:
            return redirect(req.META.get('HTTP_REFERER', '/'))

    docs = VehicleDocument.objects.filter(vehicle=curr_vehicle)
    payments = Payment.objects.filter(vehicle=curr_vehicle)
    expenses = VehicleExpense.objects.filter(vehicle=curr_vehicle)
    incidents = Incident.objects.filter(vehicle=curr_vehicle)
    total_revenu = Payment.objects.filter(vehicle=curr_vehicle).aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_expenses = VehicleExpense.objects.filter(vehicle=curr_vehicle).aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_net = total_revenu - total_expenses
    total_commission = total_revenu/curr_vehicle.commission
    context = {
        "vehicles_page": "active",
        'title': 'vehicle details',
        'curr_vehicle': curr_vehicle,
        'docs': docs,
        'payments': payments,
        'expenses': expenses,
        'incidents': incidents,
        'total_revenu': total_revenu/100,
        'total_expenses': total_expenses/100,
        'total_commission': total_commission/100,
        'total_net': total_net,

    }
    return render(req, 'base/vehicle.html', context)


@login_required(login_url='login')
def vehicle_activation(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            vehicle = Vehicle.objects.get(plate_number=pk)
            if vehicle.is_active == False:
                Vehicle.objects.filter(plate_number=pk).update(is_active=True)
            else:
                Vehicle.objects.filter(plate_number=pk).update(is_active=False)
        except Vehicle.DoesNotExist:
            return HttpResponse('Vehicle not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def create_vehicle(req):
    user = req.user
    if user.role.sec_level < 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 2:
        is_partner = Partner.objects.get(user=user)
        if not is_partner:
            return redirect('create_partner')
        else:
            form = VehicleForm()
            if req.method == 'POST':
                form = VehicleForm(req.POST, req.FILES)
                form.instance.owner = user
                if form.is_valid():
                    print('valid form')
                    form.save()
                    return redirect('vehicles')
    else:
        form = VehicleForm()
        if req.method == 'POST':
            form = VehicleForm(req.POST, req.FILES)
            if form.is_valid():
                form.save()
                return redirect('vehicles')
    context = {
        "vehicles_page": "active", "title": 'create vehicle', "form": form}
    return render(req, 'base/vehicle.html', context)


@login_required(login_url='login')
def edit_vehicle(req, pk):
    user = req.user
    curr_vehicle = Vehicle.objects.get(plate_number=pk)
    if curr_vehicle.owner != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    else:
        form = VehicleForm(instance=curr_vehicle)
        if req.method == 'POST':
            form = VehicleForm(req.POST, req.FILES, instance=curr_vehicle)
            # print(form.plate_number)
            if form.is_valid():
                print('valid form')
                form.save()
                return redirect('vehicles')
            else:
                messages.error(req, form.errors)
    context = {
        "vehicles_page": "active",
        "title": 'edit vehicle',
        "form": form,
        "curr_vehicle": curr_vehicle
    }
    return render(req, 'base/vehicle.html', context)


@login_required(login_url='login')
def delete_vehicle(req, pk):
    obj = Vehicle.objects.get(plate_number=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# -------------------------------------------------------------------- documents CRUD --------------------------------------------------------


@login_required(login_url='login')
def documents(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    else:
        d_docs = DriverDocument.objects.all()
        p_docs = PartnerDocument.objects.all()
        v_docs = VehicleDocument.objects.all()
    ordering = ['date_added']

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
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 1:
        curr_driver = Driver.objects.get(user=user)
        if not curr_driver:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        documents = DriverDocument.objects.filter(
            Q(type__name__icontains=query)
            | Q(issue_date__icontains=query)
            | Q(expiry_date__icontains=query), driver=curr_driver
        )
    else:
        documents = DriverDocument.objects.filter(
            Q(driver__first_name__icontains=query)
            | Q(driver__last_name__icontains=query)
            | Q(type__name__icontains=query)
            | Q(issue_date__icontains=query)
            | Q(expiry_date__icontains=query)
        )
    ordering = ['date_added']

    context = {
        "documents_page": "active",
        'title': 'driver documents',
        'documents': documents,
        'ordering': ordering,
    }
    return render(req, 'base/documents/driver_docs.html', context)


@login_required(login_url='login')
def driver_doc(req, pk):
    user = req.user
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 1:
        curr_driver = Driver.objects.get(user=user)
        if not curr_driver:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        curr_doc = DriverDocument.objects.get(id=pk)
        rel_documents = DriverDocument.objects.filter(
            driver=curr_doc.driver).exclude(id=pk, driver=curr_driver)
    else:
        curr_doc = DriverDocument.objects.get(id=pk)
        rel_documents = DriverDocument.objects.filter(
            driver=curr_doc.driver).exclude(id=pk)
    context = {
        "documents_page": "active",
        'title': 'driver document',
        'curr_doc': curr_doc,
        'rel_documents': rel_documents,

    }
    return render(req, 'base/documents/driver_doc.html', context)


@login_required(login_url='login')
def create_ddoc(req):
    user = req.user
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 2:
        form = DriverDocumentForm()
        if req.method == 'POST':
            form = DriverDocumentForm(req.POST, req.FILES)
            form.instance.driver = user
            if form.is_valid():
                form.save()
                return redirect('documents')
    else:
        form = DriverDocumentForm()
        if req.method == 'POST':
            form = DriverDocumentForm(req.POST, req.FILES)
            if form.is_valid():
                form.save()
                return redirect('documents')

    context = {
        "documents_page": "active",
        "title": 'create driver document',
        "form": form,
    }
    return render(req, 'base/documents/driver_doc.html', context)


@login_required(login_url='login')
def edit_ddoc(req, pk):
    user = req.user
    curr_doc = DriverDocument.objects.get(id=pk)
    if curr_doc.driver.user != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DriverDocumentForm(instance=curr_doc)
    if req.method == 'POST':
        form = DriverDocumentForm(req.POST, req.FILES, instance=curr_doc)
        if form.is_valid():
            form.save()
            return redirect('documents')

    context = {
        "documents_page": "active",
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
    if user.role.sec_level == 1:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 2:
        curr_partner = Partner.objects.get(user=user)
        if not curr_partner:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        documents = PartnerDocument.objects.filter(
            Q(type__name__icontains=query)
            | Q(issue_date__icontains=query)
            | Q(expiry_date__icontains=query), partner=curr_partner
        )
    else:
        documents = PartnerDocument.objects.filter(
            Q(partner__first_name__icontains=query)
            | Q(partner__last_name__icontains=query)
            | Q(type__name__icontains=query)
            | Q(issue_date__icontains=query)
            | Q(expiry_date__icontains=query)
        )
    ordering = ['date_added']

    context = {
        "documents_page": "active",
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
        "documents_page": "active",
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
        form = PartnerDocumentForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents')

    context = {
        "documents_page": "active",
        "title": 'create_driver_document',
        "form": form,
    }
    return render(req, 'base/documents/partner_doc.html', context)


@login_required(login_url='login')
def edit_pdoc(req, pk):
    user = req.user
    curr_doc = PartnerDocument.objects.get(id=pk)
    if curr_doc.partner.user != user and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PartnerDocumentForm(instance=curr_doc)
    if req.method == 'POST':
        form = PartnerDocumentForm(req.POST, req.FILES, instance=curr_doc)
        if form.is_valid():
            form.save()
            return redirect('documents')

    context = {
        "documents_page": "active",
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
    ordering = ['date_added']

    context = {
        "documents_page": "active",
        'title': 'vehicle documents',
        'documents': documents,
        'ordering': ordering,
    }
    return render(req, 'base/documents/vehicle_docs.html', context)


login_required(login_url='login')


def create_vdoc(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    else:
        form = VehicleDocumentForm()
        if req.method == 'POST':
            form = VehicleDocumentForm(req.POST, req.FILES)
            if form.is_valid():
                form.save()
                return redirect('documents')

    context = {
        "documents_page": "active",
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
        "documents_page": "active",
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
        form = VehicleDocumentForm(req.POST, req.FILES, instance=curr_doc)
        if form.is_valid():
            form.save()
            return redirect('documents')
    context = {
        "documents_page": "active",
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
    if user.role.sec_level == 1:
        curr_driver = Driver.objects.get(user=user)
        if not curr_driver:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        incidents = Incident.objects.filter(
            Q(vehicle__plate_number__icontains=query) |
            Q(vehicle__model__icontains=query) |
            Q(vehicle__make__icontains=query),
            driver=curr_driver
        ).order_by('date_added')

        incident_count = incidents.count()
        if incident_count > 0:
            solved_count = incidents.filter(is_solved=True).count()
            unsolved_count = incidents.filter(is_solved=False).count()
            resolution_rate = solved_count * 100 / incident_count
        else:
            solved_count = 0
            unsolved_count = 0
            resolution_rate = 0

    elif user.role.sec_level == 2:
        curr_partner = Partner.objects.get(user=user)
        if not curr_partner:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        incidents = Incident.objects.filter(
            Q(vehicle__plate_number__icontains=query) |
            Q(vehicle__model__icontains=query) |
            Q(vehicle__make__icontains=query),
            vehicle__in=Vehicle.objects.filter(
                owner=curr_partner.user)).order_by('date_added')

        incident_count = incidents.count()
        if incident_count > 0:
            solved_count = incidents.filter(is_solved=True).count()
            unsolved_count = incidents.filter(is_solved=False).count()
            resolution_rate = solved_count * 100 / incident_count
        else:
            solved_count = 0
            unsolved_count = 0
            resolution_rate = 0

    else:
        incidents = Incident.objects.filter(
            Q(vehicle__plate_number__icontains=query)
            | Q(vehicle__model__icontains=query)
            | Q(vehicle__make__icontains=query)
            | Q(driver__first_name__icontains=query)
            | Q(driver__first_name__icontains=query)
        ).order_by('date_added')
        incident_count = Incident.objects.count()
        if incident_count > 0:
            solved_count = incidents.filter(is_solved=True).count()
            unsolved_count = incidents.filter(is_solved=False).count()
            resolution_rate = solved_count * 100 / incident_count
        else:
            solved_count = 0
            unsolved_count = 0
            resolution_rate = 0

    context = {
        "incidents_page": "active",
        'title': 'incidents',
        'incidents': incidents,
        'incident_count': incident_count,
        'solved_count': solved_count,
        'unsolved_count': unsolved_count,
        'resolution_rate': resolution_rate,
    }
    return render(req, 'base/incidents.html', context)


@login_required(login_url='login')
def incident(req, pk):
    user = req.user
    curr_incident = Incident.objects.get(id=pk)
    rel_incidents = Incident.objects.filter(vehicle=curr_incident.vehicle)
    context = {
        "incidents_page": "active",
        'title': 'incident',
        'curr_incident': curr_incident,
        'rel_incidents': rel_incidents,

    }
    return render(req, 'base/incident.html', context)


@login_required(login_url='login')
def incident_resolution(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            incident = Incident.objects.get(id=pk)
            if incident.is_solved == False:
                Incident.objects.filter(id=pk).update(is_solved=True)
            else:
                Incident.objects.filter(id=pk).update(is_solved=False)
        except Incident.DoesNotExist:
            return HttpResponse('Vehicle not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def create_incident(req):
    user = req.user
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = IncidentForm()
    if req.method == 'POST':
        form = IncidentForm(req.POST, req.FILES)
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('incidents')
    context = {
        "incidents_page": "active",
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
        form = IncidentForm(req.POST, req.FILES, instance=curr_incident)
        if form.is_valid():
            form.save()
            return redirect('incidents')
    context = {
        "incidents_page": "active",
        "title": 'edit_incident',
        "form": form,
        "curr_incident": curr_incident
    }
    return render(req, 'base/incident.html', context)


@login_required(login_url='login')
def delete_incident(req, pk):
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj = Incident.objects.get(id=pk)
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

# -------------------------------------------------------------------- parameters CRUD --------------------------------------------------------


@login_required(login_url='login')
def parameters(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    doc_types = DocumentType.objects.all()
    incid_types = IncidentType.objects.all()
    company = Company.objects.first()
    roles = Role.objects.all()
    context = {
        "parameters_page": "active",
        "title": 'parameters',
        "doc_types": doc_types,
        "incid_types": incid_types,
        "company": company,
        "roles": roles
    }
    return render(req, 'parameters/index.html', context)

# -------------------------------------------------------------------- types of documents


@login_required(login_url='login')
def create_doc_type(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DocTypeForm()
    if req.method == 'POST':
        form = DocTypeForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('parameters')
    context = {
        "parameters_page": "active",
        "title": 'create document type',
        "form": form
    }
    return render(req, 'parameters/document.html', context)


@login_required(login_url='login')
def edit_doc_type(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    curr_doc = DocumentType.objects.get(id=pk)
    form = DocTypeForm(instance=curr_doc)
    if req.method == 'POST':
        form = DocTypeForm(req.POST, req.FILES, instance=curr_doc)
        if form.is_valid():
            form.save()
            return redirect('parameters')
    context = {
        "parameters_page": "active",
        "title": 'edit document type',
        "curr_doc": curr_doc,
        "form": form
    }
    return render(req, 'parameters/document.html', context)


@login_required(login_url='login')
def delete_doc_type(req, pk):
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj = DocumentType.objects.get(id=pk)
    obj.delete()
    return redirect('parameters')
# -------------------------------------------------------------------- types of incid_types


@login_required(login_url='login')
def create_incident_type(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = IncidentTypeForm()
    if req.method == 'POST':
        form = IncidentTypeForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('parameters')
    context = {
        "parameters_page": "active",
        "title": 'create incident type',
        "form": form
    }
    return render(req, 'parameters/incident.html', context)


@login_required(login_url='login')
def edit_incident_type(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    curr_doc = IncidentType.objects.get(id=pk)
    form = IncidentTypeForm(instance=curr_doc)
    if req.method == 'POST':
        form = IncidentTypeForm(req.POST, req.FILES, instance=curr_doc)
        if form.is_valid():
            form.save()
            return redirect('parameters')
    context = {
        "parameters_page": "active",
        "title": 'edit document type',
        "curr_doc": curr_doc,
        "form": form
    }
    return render(req, 'parameters/incident.html', context)


@login_required(login_url='login')
def delete_incident_type(req, pk):
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj = IncidentType.objects.get(id=pk)
    obj.delete()
    return redirect('parameters')

# -------------------------------------------------------------------- comopany


@login_required(login_url='login')
def create_company(req):
    user = req.user
    if user.role.sec_level < 4:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = CompanyForm()
    if req.method == 'POST':
        form = CompanyForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('parameters')
    context = {
        "parameters_page": "active",
        "title": 'create company',
        "form": form
    }
    return render(req, 'parameters/company.html', context)


@login_required(login_url='login')
def edit_company(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    curr_obj = Company.objects.get(id=pk)
    form = CompanyForm(instance=curr_obj)
    if req.method == 'POST':
        form = CompanyForm(req.POST, req.FILES, instance=curr_obj)
        if form.is_valid():
            form.save()
            return redirect('parameters')
    context = {
        "parameters_page": "active",
        "title": 'edit company',
        "curr_obj": curr_obj,
        "form": form
    }
    return render(req, 'parameters/company.html', context)


@login_required(login_url='login')
def delete_company(req, pk):
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj = Company.objects.get(id=pk)
    obj.delete()
    return redirect('parameters')


# notifications------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def notifications(req):
    user = req.user
    notifications = Notification.objects.filter(
        user=user, is_read=False).order_by('-timestamp')

    context = {
        'notifications_page': 'active',
        'notifications': notifications,
    }
    return render(req, 'base/notifications.html', context)


# video materials------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
def tips(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    tips = Tip.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query),
    )

    context = {
        "tips_page": "active",
        'title': 'tips',
        'tips': tips,

    }
    return render(req, 'base/tips.html', context)


@login_required(login_url='login')
def tip(req, pk):
    user = req.user
    curr_tip = Tip.objects.get(id=pk)
    rel_tips = Tip.objects.all().exclude(id=curr_tip.id)
    context = {
        "tips_page": "active",
        'title': 'tips',
        'curr_tip': curr_tip,
        'rel_tips': rel_tips,

    }
    return render(req, 'base/tip.html', context)


@login_required(login_url='login')
def create_tip(req):
    user = req.user
    if user.role.sec_level < 4:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = TipForm()
    if req.method == 'POST':
        form = TipForm(req.POST, req.FILES)
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('tips')
    context = {
        "tips_page": "active",
        "title": 'create tip',
        "form": form
    }
    return render(req, 'base/tip.html', context)


@login_required(login_url='login')
def edit_tip(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    curr_obj = Tip.objects.get(id=pk)
    form = TipForm(instance=curr_obj)
    if req.method == 'POST':
        form = TipForm(req.POST, req.FILES, instance=curr_obj)
        if form.is_valid():
            form.save()
            return redirect('tips')
    context = {
        "tips_page": "active",
        "title": 'edit tip',
        "curr_obj": curr_obj,
        "form": form
    }
    return render(req, 'base/tip.html', context)


@login_required(login_url='login')
def delete_tip(req, pk):
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj = Tip.objects.get(id=pk)
    obj.delete()
    return redirect('tips')
