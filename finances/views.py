from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Min, Max
import csv
# from finances.forms import LedgerForm

from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.


@login_required(login_url='login')
def finances(req):
    user = req.user
    if user.role.sec_level == 1:
        curr_driver = Driver.objects.get(user=user)
        d_expenses = DriverExpense.objects.filter(driver=curr_driver).count()
        v_expenses = VehicleExpense.objects.filter(
            vehicle__in=Vehicle.objects.filter(owner=user)).count()
        g_expenses = GlobalExpense.objects.none().count()
        payments = Payment.objects.filter(
            vehicle__in=Vehicle.objects.filter(owner=user)).count()
        payouts = Payout.objects.filter(driver=curr_driver).count()
        transactions = payments + v_expenses
    if user.role.sec_level == 2:
        d_expenses = DriverExpense.objects.none().count()
        v_expenses = VehicleExpense.objects.filter(
            vehicle__in=Vehicle.objects.filter(owner=user)).count()
        g_expenses = GlobalExpense.objects.none().count()
        payments = Payment.objects.filter(
            vehicle__in=Vehicle.objects.filter(owner=user)).count()
        payouts = Payout.objects.none().count()
        transactions = payments + v_expenses
    else:
        d_expenses = DriverExpense.objects.filter().count()
        v_expenses = VehicleExpense.objects.all().count()
        g_expenses = GlobalExpense.objects.all().count()
        payments = Payment.objects.all().count()
        payouts = Payout.objects.all().count()
        transactions = payments + payouts

    context = {
        "finance_page": "active",
        'title': 'finances',
        'd_expenses': d_expenses,
        'v_expenses': v_expenses,
        'g_expenses': g_expenses,
        'payments': payments,
        'payouts': payouts,
        'transactions': transactions,

    }
    return render(req, 'finances/index.html', context)


# --------------------------------------------------------- expenses CRUD ---------------------------------------------------------


@login_required(login_url='login')
def expenses(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    d_expenses = DriverExpense.objects.all().order_by('date')
    v_expenses = VehicleExpense.objects.all().order_by('date')
    g_expenses = GlobalExpense.objects.all().order_by('date')

    context = {
        "finance_page": "active",
        'title': 'expenses',
        'd_expenses': d_expenses,
        'v_expenses': v_expenses,
        'g_expenses': g_expenses,

    }
    return render(req, 'finances/expenses/index.html', context)


# -------------------------------- driver expenses ------------------------------------


@login_required(login_url='login')
def d_expenses(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 1:
        curr_driver = Driver.objects.get(user=user)
        if not curr_driver:
            return redirect('create_driver')
        else:
            expenses = DriverExpense.objects.filter(
                Q(amount__icontains=query)
                | Q(details__icontains=query), driver=curr_driver
            ).order_by('date')
    else:
        expenses = DriverExpense.objects.filter(
            Q(amount__icontains=query)
            | Q(details__icontains=query)
            | Q(driver__first_name__icontains=query)
            | Q(driver__last_name__icontains=query)
        ).order_by('date')

    context = {
        "finance_page": "active",
        'title': 'driver expenses',
        'expenses': expenses,

    }
    return render(req, 'finances/expenses/d_expenses.html', context)


@login_required(login_url='login')
def d_expense(req, pk):
    user = req.user
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    elif user.role.sec_level == 1:
        curr_driver = Driver.objects.get(user=user)
        if not curr_driver:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        else:
            curr_expense = DriverExpense.objects.get(id=pk, driver=curr_driver)
            rel_expenses = DriverExpense.objects.filter(
                driver=curr_expense.driver).exclude(id=pk, driver=curr_driver)

    else:
        curr_expense = DriverExpense.objects.get(id=pk)
        rel_expenses = DriverExpense.objects.filter(
            driver=curr_expense.driver).exclude(id=pk)
    context = {
        "finance_page": "active",
        'title': 'driver expense',
        'curr_expense': curr_expense,
        'rel_expenses': rel_expenses,

    }
    return render(req, 'finances/expenses/d_expense.html', context)


@login_required(login_url='login')
def create_d_expense(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DriverExpenseForm()
    if req.method == 'POST':
        form = DriverExpenseForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "finance_page": "active",
        "title": 'create driver expenses',
        "form": form,
    }
    return render(req, 'finances/expenses/d_expense.html', context)


@login_required(login_url='login')
def edit_d_expense(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    curr_expense = DriverExpense.objects.get(id=pk)
    if not curr_expense:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DriverExpenseForm(instance=curr_expense)
    if req.method == 'POST':
        form = DriverExpenseForm(req.POST, req.FILES, instance=curr_expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "finance_page": "active",
        "title": 'edit driver expenses',
        "form": form,
        "curr_expense": curr_expense}
    return render(req, 'finances/expenses/d_expense.html', context)


@login_required(login_url='login')
def audit_d_expense(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            obj = DriverExpense.objects.get(id=pk)
            if obj.is_audited == False:
                DriverExpense.objects.filter(id=pk).update(is_audited=True)
            else:
                DriverExpense.objects.filter(id=pk).update(is_audited=False)
        except DriverExpense.DoesNotExist:
            return HttpResponse('Driver Expense not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def delete_d_expense(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    obj = DriverExpense.objects.get(id=pk)
    obj.delete()
    return redirect('d_expenses')


@login_required(login_url='login')
def d_expenses_csv(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachement; filename=depenses_conducteurs.csv'
    # create csv writer
    writer = csv.writer(res)
    # designate the model(s) of interest
    objs = DriverExpense.objects.all()
    # add column headings
    writer.writerow(['ID_Caisse', 'Type de Caisse', 'Conducteur', 'Titre',
                    'Détails', 'Montant', 'Date', 'Heure', 'Status'])
    for col in objs:
        writer.writerow([col.vault, col.vault.type, col.driver.first_name, col.title,
                        col.details, col.amount, col.date, col.time, col.is_audited])
    return res

# -------------------------------- vehicle expenses ------------------------------------


@login_required(login_url='login')
def v_expenses(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''

    if user.role.sec_level < 2:
        curr_driver = Driver.objects.get(user=user)
        if not curr_driver:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        expenses = VehicleExpense.objects.filter(
            Q(amount__icontains=query)
            | Q(details__icontains=query)
            | Q(vehicle__model__icontains=query)
            | Q(vehicle__make__icontains=query),
            vehicle__in=Vehicle.objects.filter(
                Q(first_driver=curr_driver)
                | Q(second_driver=curr_driver)
                | Q(third_driver=curr_driver)
            )
        ).order_by('date')
    elif user.role.sec_level == 2:
        curr_partner = Partner.objects.get(user=user)
        if not curr_partner:
            return redirect(req.META.get('HTTP_REFERER', '/'))
        expenses = VehicleExpense.objects.filter(
            Q(amount__icontains=query)
            | Q(details__icontains=query)
            | Q(vehicle__model__icontains=query)
            | Q(vehicle__make__icontains=query),
            vehicle__in=Vehicle.objects.filter(owner=user)
        ).order_by('date')
    else:
        expenses = VehicleExpense.objects.filter(
            Q(amount__icontains=query)
            | Q(details__icontains=query)
            | Q(vehicle__model__icontains=query)
            | Q(vehicle__make__icontains=query)
        ).order_by('date')

    context = {
        "finance_page": "active",
        'title': 'vehicle expenses',
        'expenses': expenses,

    }
    return render(req, 'finances/expenses/v_expenses.html', context)


@login_required(login_url='login')
def v_expense(req, pk):
    user = req.user
    curr_expense = VehicleExpense.objects.get(id=pk)
    rel_expenses = VehicleExpense.objects.filter(
        vehicle=curr_expense.vehicle).exclude(id=pk)
    context = {
        "finance_page": "active",
        'title': 'vehicle expense',
        'curr_expense': curr_expense,
        'rel_expenses': rel_expenses,

    }
    return render(req, 'finances/expenses/v_expense.html', context)


@login_required(login_url='login')
def create_v_expense(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VehicleExpenseForm()
    if req.method == 'POST':
        form = VehicleExpenseForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "finance_page": "active",
        "title": 'create vehicle expenses',
        "form": form,
    }
    return render(req, 'finances/expenses/v_expense.html', context)


@login_required(login_url='login')
def edit_v_expense(req, pk):
    user = req.user
    curr_expense = VehicleExpense.objects.get(id=pk)
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VehicleExpenseForm(instance=curr_expense)
    if req.method == 'POST':
        form = VehicleExpenseForm(req.POST, req.FILES, instance=curr_expense)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('expenses')

    context = {
        "finance_page": "active",
        "title": 'edit vehicle expenses',
        "form": form,
        "curr_expense": curr_expense}
    return render(req, 'finances/expenses/v_expense.html', context)


@login_required(login_url='login')
def audit_v_expense(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            obj = VehicleExpense.objects.get(id=pk)
            if obj.is_audited == False:
                VehicleExpense.objects.filter(id=pk).update(is_audited=True)
            else:
                VehicleExpense.objects.filter(id=pk).update(is_audited=False)
        except VehicleExpense.DoesNotExist:
            return HttpResponse('Vehicle Expense not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def delete_v_expense(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    obj = VehicleExpense.objects.get(id=pk)
    obj.delete()
    return redirect('v_expenses')


@login_required(login_url='login')
def v_expenses_csv(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachement; filename=depenses_véhicules.csv'
    # create csv writer
    writer = csv.writer(res)
    # designate the model(s) of interest
    objs = VehicleExpense.objects.all()
    # add column headings
    writer.writerow(['ID_Caisse', 'Type de Caisse', 'Véhicule', 'Titre',
                    'Détails', 'Montant', 'Date', 'Heure', 'Status'])
    for col in objs:
        writer.writerow([col.vault, col.vault.type, col.vehicle.plate_number, col.title,
                        col.details, col.amount, col.date, col.time, col.is_audited])
    return res

# -------------------------------- global expenses ------------------------------------


@login_required(login_url='login')
def g_expenses(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    query = req.GET.get('query') if req.GET.get('query') != None else ''
    expenses = GlobalExpense.objects.filter(
        Q(amount__icontains=query)
        | Q(details__icontains=query)
        | Q(author__first_name__icontains=query)
        | Q(author__last_name__icontains=query)
    ).order_by('date')

    context = {
        "finance_page": "active",
        'title': 'expenses',
        'expenses': expenses,

    }
    return render(req, 'finances/expenses/g_expenses.html', context)


@login_required(login_url='login')
def g_expense(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    curr_expense = GlobalExpense.objects.get(id=pk)
    rel_expenses = GlobalExpense.objects.filter(
        author=curr_expense.author).exclude(id=pk)
    context = {
        "finance_page": "active",
        'title': 'driver expense',
        'curr_expense': curr_expense,
        'rel_expenses': rel_expenses,

    }
    return render(req, 'finances/expenses/g_expense.html', context)


@login_required(login_url='login')
def create_g_expense(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = GlobalExpenseForm()
    if req.method == 'POST':
        form = GlobalExpenseForm(req.POST, req.FILES)
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "finance_page": "active",
        "title": 'create global expenses',
        "form": form,
    }
    return render(req, 'finances/expenses/g_expense.html', context)


@login_required(login_url='login')
def edit_g_expense(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    curr_expense = GlobalExpense.objects.get(id=pk)
    form = GlobalExpenseForm(instance=curr_expense)
    if req.method == 'POST':
        form = GlobalExpenseForm(req.POST, req.FILES, instance=curr_expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "finance_page": "active",
        "title": 'edit global expenses',
        "form": form,
        "curr_expense": curr_expense}
    return render(req, 'finances/expenses/g_expense.html', context)


@login_required(login_url='login')
def audit_g_expense(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            obj = GlobalExpense.objects.get(id=pk)
            if obj.is_audited == False:
                GlobalExpense.objects.filter(id=pk).update(is_audited=True)
            else:
                GlobalExpense.objects.filter(id=pk).update(is_audited=False)
        except GlobalExpense.DoesNotExist:
            return HttpResponse('Global Expense not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def delete_g_expense(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    obj = GlobalExpense.objects.get(id=pk)
    obj.delete()
    return redirect('g_expenses')


@login_required(login_url='login')
def g_expenses_csv(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachement; filename=depenses_globales.csv'
    # create csv writer
    writer = csv.writer(res)
    # designate the model(s) of interest
    objs = GlobalExpense.objects.all()
    # add column headings
    writer.writerow(['ID_Caisse', 'Type de Caisse', 'Auteur', 'Titre',
                    'Détails', 'Montant', 'Date', 'Heure', 'Status'])
    for col in objs:
        writer.writerow([col.vault, col.vault.type, col.author.last_name, col.title,
                        col.details, col.amount, col.date, col.time, col.is_audited])
    return res

# --------------------------------------------------------- transactions CRUD ---------------------------------------------------------


@login_required(login_url='login')
def transactions(req):
    user = req.user
    if user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

    payments = Payment.objects.all()
    payouts = Payout.objects.all()
    context = {
        "finance_page": "active",
        'title': 'transactions',
        'payments': payments,
        'payouts': payouts,

    }
    return render(req, 'finances/transactions/index.html', context)


# -------------------------------- driver payments ------------------------------------


@login_required(login_url='login')
def payments(req):
    user = req.user
    if user.role.sec_level == 1:
        payments = Payment.objects.filter(
            driver__in=Driver.objects.filter(user=user))

    elif user.role.sec_level == 2:
        payments = Payment.objects.filter(
            vehicle__in=Vehicle.objects.filter(owner=user))
    else:
        payments = Payment.objects.all()
    print('Payments page', payments)
    context = {
        "finance_page": "active",
        'title': 'payments',
        'payments': payments,

    }
    return render(req, 'finances/transactions/payments.html', context)


@login_required(login_url='login')
def payment(req, pk):
    user = req.user
    if user.role.sec_level == 1:
        d_driver = Driver.objects.get(user=user)
        curr_payment = Payment.objects.get(id=pk, driver=d_driver)
    elif user.role.sec_level == 2:
        curr_payment = Payment.objects.get(id=pk,
                                           vehicle__in=Vehicle.objects.filter(owner=user))
    else:
        curr_payment = Payment.objects.get(id=pk)

    rel_payments = Payment.objects.filter(
        driver=curr_payment.driver).exclude(id=pk)
    context = {
        "finance_page": "active",
        'title': 'driver_payment',
        'curr_payment': curr_payment,
        'rel_payments': rel_payments,

    }
    return render(req, 'finances/transactions/payment.html', context)


@login_required(login_url='login')
def create_payment(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PaymentForm()
    if req.method == 'POST':
        form = PaymentForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('payments')

    context = {
        "finance_page": "active",
        "title": 'create_payments',
        "form": form,
    }
    return render(req, 'finances/transactions/payment.html', context)


@login_required(login_url='login')
def edit_payment(req, pk):
    user = req.user
    curr_payment = Payment.objects.get(id=pk)
    if not curr_payment and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PaymentForm(instance=curr_payment)
    if req.method == 'POST':
        form = PaymentForm(req.POST, req.FILES, instance=curr_payment)
        if form.is_valid():
            form.save()
            return redirect('payments')

    context = {
        "finance_page": "active",
        "title": 'edit_payment',
        "form": form,
        "curr_payment": curr_payment}
    return render(req, 'finances/transactions/payment.html', context)


@login_required(login_url='login')
def audit_payment(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            obj = Payment.objects.get(id=pk)
            if obj.is_audited == False:
                Payment.objects.filter(id=pk).update(is_audited=True)
            else:
                Payment.objects.filter(id=pk).update(is_audited=False)
        except Payment.DoesNotExist:
            return HttpResponse('Payment not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def delete_payment(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    obj = Payment.objects.get(id=pk)
    obj.delete()
    return redirect('payments')


@login_required(login_url='login')
def payments_csv(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachement; filename=versements.csv'
    # create csv writer
    writer = csv.writer(res)
    # designate the model(s) of interest
    objs = Payment.objects.all()
    # add column headings
    writer.writerow(['ID_Caisse', 'Type de Caisse', 'Conducteur', 'Véhicule', 'Montant',
                     'Jour', 'Heure de début', 'Heure de fin',  'Date payé', 'Status'])
    for col in objs:
        writer.writerow([col.vault, col.vault.type, col.driver.first_name, col.vehicle.plate_number, col.amount,
                         col.date, col.start_time, col.end_time, col.payday, col.is_audited])
    return res


# -------------------------------- driver payouts ------------------------------------

@login_required(login_url='login')
def payouts(req):
    user = req.user
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 1:
        payouts = Payout.objects.filter(
            driver__in=Driver.objects.filter(user=user))
    else:
        payouts = Payout.objects.all()
    context = {
        "finance_page": "active",
        'title': 'driver payouts',
        'payouts': payouts,

    }
    return render(req, 'finances/transactions/payouts.html', context)


@login_required(login_url='login')
def payout(req, pk):
    user = req.user
    if user.role.sec_level == 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 1:
        curr_driver = Driver.objects.get(user=user)
        curr_payout = Payout.objects.get(id=pk, driver=curr_driver)
    else:
        curr_payout = Payout.objects.get(id=pk)

    rel_payouts = Payout.objects.filter(
        driver=curr_payout.driver).exclude(id=pk)
    context = {
        "finance_page": "active",
        'title': 'driver_payout',
        'curr_payout': curr_payout,
        'rel_payouts': rel_payouts,

    }
    return render(req, 'finances/transactions/payout.html', context)


@login_required(login_url='login')
def create_payout(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PayoutForm()
    if req.method == 'POST':
        form = PayoutForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('payouts')

    context = {
        "finance_page": "active",
        "title": 'create_payouts',
        "form": form,
    }
    return render(req, 'finances/transactions/payout.html', context)


@login_required(login_url='login')
def edit_payout(req, pk):
    user = req.user
    curr_payout = Payout.objects.get(id=pk)
    if not curr_payout and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PayoutForm(instance=curr_payout)
    if req.method == 'POST':
        form = PayoutForm(req.POST, req.FILES, instance=curr_payout)
        if form.is_valid():
            form.save()
            return redirect('payouts')

    context = {
        "finance_page": "active",
        "title": 'edit_payout',
        "form": form,
        "curr_payout": curr_payout}
    return render(req, 'finances/transactions/payout.html', context)


@login_required(login_url='login')
def audit_payout(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            obj = Payout.objects.get(id=pk)
            if obj.is_audited == False:
                Payout.objects.filter(id=pk).update(is_audited=True)
            else:
                Payout.objects.filter(id=pk).update(is_audited=False)
        except Payout.DoesNotExist:
            return HttpResponse('Payout not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def delete_payout(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    obj = Payout.objects.get(id=pk)
    obj.delete()
    return redirect('payouts')


@login_required(login_url='login')
def payouts_csv(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachement; filename=paiements.csv'
    # create csv writer
    writer = csv.writer(res)
    # designate the model(s) of interest
    objs = Payout.objects.all()
    # add column headings
    writer.writerow(['ID_Caisse', 'Type de Caisse', 'Conducteur', 'Jours ouvrés',
                     'Date de début', 'Date de fin', 'Montant', 'Date payé', 'Status'])
    for col in objs:
        writer.writerow([col.vault, col.vault.type, col.driver.first_name, col.days_worked,
                         col.start_date, col.end_date, col.amount, col.payday, col.is_audited])
    return res

# -------------------------------- partner revenues ------------------------------------


@login_required(login_url='login')
def revenues(req):
    user = req.user
    if user.role.sec_level < 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    elif user.role.sec_level == 2:
        revenues = Revenue.objects.filter(
            driver__in=Driver.objects.filter(user=user.driver))
    else:
        revenues = Revenue.objects.all()
    context = {
        "finance_page": "active",
        'title': 'driver revenues',
        'revenues': revenues,

    }
    return render(req, 'finances/accounting/revenues.html', context)


@login_required(login_url='login')
def revenue(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    curr_revenue = Revenue.objects.get(id=pk)
    rel_revenues = Revenue.objects.filter(
        driver=curr_revenue.driver).exclude(id=pk)
    context = {
        "finance_page": "active",
        'title': 'partner revenue',
        'curr_revenue': curr_revenue,
        'rel_revenues': rel_revenues,

    }
    return render(req, 'finances/accounting/revenue.html', context)


@login_required(login_url='login')
def create_revenue(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = RevenueForm()
    if req.method == 'POST':
        form = RevenueForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('revenues')

    context = {
        "finance_page": "active",
        "title": 'create partner revenue',
        "form": form,
    }
    return render(req, 'finances/accounting/revenue.html', context)


@login_required(login_url='login')
def edit_revenue(req, pk):
    user = req.user
    curr_revenu = Revenue.objects.get(id=pk)
    if not curr_revenu and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = RevenueForm(instance=curr_revenu)
    if req.method == 'POST':
        form = RevenueForm(req.POST, req.FILES, instance=curr_revenu)
        if form.is_valid():
            form.save()
            return redirect('revenues')

    context = {
        "finance_page": "active",
        "title": 'edit_revenue',
        "form": form,
        "curr_revenu": curr_revenu}
    return render(req, 'finances/accounting/revenue.html', context)


@login_required(login_url='login')
def audit_revenue(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            obj = Revenue.objects.get(id=pk)
            if obj.is_audited == False:
                Revenue.objects.filter(id=pk).update(is_audited=True)
            else:
                Revenue.objects.filter(id=pk).update(is_audited=False)
        except Revenue.DoesNotExist:
            return HttpResponse('Revenue not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def delete_revenue(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    obj = Revenue.objects.get(id=pk)
    obj.delete()
    return redirect('revenues')


@login_required(login_url='login')
def revenues_csv(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachement; filename=revenues.csv'
    # create csv writer
    writer = csv.writer(res)
    # designate the model(s) of interest
    objs = Revenue.objects.all()
    # add column headings
    writer.writerow(['ID_Caisse', 'Type de Caisse', 'Conducteur', 'Véhicule', 'Jours ouvrés',
                     'Revenue Brut', 'Revenue net', 'Date payé', 'Status'])
    for col in objs:
        writer.writerow([col.vault, col.vault.type, col.partner.first_name, col.vehicle.plate_number,
                         col.days_worked, col.gross_income, col.net_income, col.payday, col.is_audited])
    return res


# --------------------------------------------------------- bookkeeping CRUD ---------------------------------------------------------

# -------------------------------- balancesheet ------------------------------------


@login_required(login_url='login')
def balancesheet(req):
    user = req.user
    if user.role.sec_level < 2:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

    elif user.role.sec_level == 2:
        payments = Payment.objects.filter(
            vehicle__in=Vehicle.objects.filter(owner=user))
        payouts = Payout.objects.all()
        d_expenses = DriverExpense.objects.none()
        v_expenses = VehicleExpense.objects.filter(
            vehicle__in=Vehicle.objects.filter(owner=user))
        g_expenses = GlobalExpense.objects.none()
        payments_count = payments.count()
        payouts_count = Payout.objects.none().count()
        d_expenses_count = DriverExpense.objects.none().count()
        v_expenses_count = v_expenses.count()
        g_expenses_count = GlobalExpense.objects.none().count()

    else:
        payments = Payment.objects.all()
        payouts = Payout.objects.all()
        d_expenses = DriverExpense.objects.all()
        v_expenses = VehicleExpense.objects.all()
        g_expenses = GlobalExpense.objects.all()
        payments_count = Payment.objects.all().count()
        payouts_count = Payout.objects.all().count()
        d_expenses_count = DriverExpense.objects.all().count()
        v_expenses_count = VehicleExpense.objects.all().count()
        g_expenses_count = GlobalExpense.objects.all().count()

    transactions = payments_count + payouts_count + \
        d_expenses_count + v_expenses_count + g_expenses_count
    # --------------------------------------------------------credit / payments--------------------------------------------------------
    total_payment = payments.aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_payment = payments.aggregate(Max('amount'))[
        'amount__max'] or 0
    min_payment = payments.aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_payment = payments.aggregate(Avg('amount'))[
        'amount__avg'] or 0

    # --------------------------------------------------------debit--------------------------------------------------------

    # payouts--------------------------------------------------------
    total_payout = payouts.aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_payout = payouts.aggregate(Max('amount'))[
        'amount__max'] or 0
    min_payout = payouts.aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_payout = payouts.aggregate(Avg('amount'))[
        'amount__avg'] or 0

    # expenses--------------------------------------------------------
    total_d_expenses = d_expenses.aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_d_expense = d_expenses.aggregate(Max('amount'))[
        'amount__max'] or 0
    min_d_expense = d_expenses.aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_d_expense = d_expenses.aggregate(Avg('amount'))[
        'amount__avg'] or 0

    total_v_expenses = v_expenses.aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_v_expense = v_expenses.aggregate(Max('amount'))[
        'amount__max'] or 0
    min_v_expense = v_expenses.aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_v_expense = v_expenses.aggregate(Avg('amount'))[
        'amount__avg'] or 0

    total_g_expenses = g_expenses.aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_g_expense = g_expenses.aggregate(Max('amount'))[
        'amount__max'] or 0
    min_g_expense = g_expenses.aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_g_expense = g_expenses.aggregate(Avg('amount'))[
        'amount__avg'] or 0

    # balance
    total_credit = total_payment
    if user.role.sec_level == 2:
        total_debit = total_v_expenses
    else:
        total_debit = total_payout + total_d_expenses + \
            total_v_expenses + total_g_expenses

    total_balance = total_credit - total_debit

    context = {
        "finance_page": "active",
        'title': 'company balancesheet',
        'payments': payments,
        'payouts': payouts,
        'd_expenses': d_expenses,
        'v_expenses': v_expenses,
        'g_expenses': g_expenses,
        'payments_count': payments_count,
        'payouts_count': payouts_count,
        'd_expenses_count': d_expenses_count,
        'v_expenses_count': v_expenses_count,
        'g_expenses_count': g_expenses_count,
        'transactions': transactions,

        # credit
        'total_payment': total_payment,
        'max_payment': max_payment,
        'min_payment': min_payment,
        'avg_payment': avg_payment,

        # debit
        'total_payout': total_payout,
        'max_payout': max_payout,
        'min_payout': min_payout,
        'avg_payout': avg_payout,

        # d_expenses
        'total_d_expenses': total_d_expenses,
        'max_d_expense': max_d_expense,
        'min_d_expense': min_d_expense,
        'avg_d_expense': avg_d_expense,

        # v_expenses
        'total_v_expenses': total_v_expenses,
        'max_v_expense': max_v_expense,
        'min_v_expense': min_v_expense,
        'avg_v_expense': avg_v_expense,

        # g_expenses
        'total_g_expenses': total_g_expenses,
        'max_g_expense': max_g_expense,
        'min_g_expense': min_g_expense,
        'avg_g_expense': avg_g_expense,

        # balance
        'total_credit': total_credit,
        'total_debit': total_debit,
        'total_balance': total_balance,

    }
    return render(req, 'finances/accounting/balancesheet.html', context)


# -------------------------------- audits ------------------------------------
@login_required(login_url='login')
def audit(req):
    user = req.user
    if user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

    payments = Payment.objects.all().all().order_by('-payday')
    payouts = Payout.objects.all().all().order_by('-payday')
    d_expenses = DriverExpense.objects.all().order_by('-date')
    v_expenses = VehicleExpense.objects.all().order_by('-date')
    g_expenses = GlobalExpense.objects.all().order_by('-date')
    context = {
        "finance_page": "active",
        'title': 'audits',
        'payments': payments,
        'payouts': payouts,
        'd_expenses': d_expenses,
        'v_expenses': v_expenses,
        'g_expenses': g_expenses,

    }
    return render(req, 'finances/accounting/audit.html', context)


@login_required(login_url='login')
def stats(req):
    user = req.user
    if user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

    drivers = Driver.objects.all()
    partners = Partner.objects.all()
    vehicles = Vehicle.objects.all()
    # -------------
    for obj in vehicles:
        v_revenue = Payment.objects.filter(vehicle__in=Vehicle.objects.filter(plate_number=obj.plate_number)).aggregate(Sum('amount'))[
            'amount__sum'] or 0
    # -------------
    d_exp_count = DriverExpense.objects.all().count()
    v_exp_count = VehicleExpense.objects.all().count()
    g_exp_count = GlobalExpense.objects.all().count()
    # -------------
    d_exp_sum = DriverExpense.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    v_exp_sum = VehicleExpense.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    g_exp_sum = GlobalExpense.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    # -------------
    payments_count = Payment.objects.all().count()
    payouts_count = Payout.objects.all().count()
    transactions = payments_count + payouts_count
    # debit--------------------------------------------------------
    total_payout = Payout.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_d_expenses = DriverExpense.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_v_expenses = VehicleExpense.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_g_expenses = GlobalExpense.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    total_debit = total_payout + total_d_expenses + \
        total_v_expenses + total_g_expenses
    # credit--------------------------------------------------------
    total_credit = Payment.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0

    context = {
        "stats_page": "active",
        'title': 'stats',
        'payments_count': payments_count,
        'payouts_count': payouts_count,
        #
        'd_exp_count': d_exp_count,
        'v_exp_count': v_exp_count,
        'g_exp_count': g_exp_count,
        #
        'd_exp_sum': d_exp_sum/1000,
        'v_exp_sum': v_exp_sum/1000,
        'g_exp_sum': g_exp_sum/1000,
        #
        'total_d_expenses': total_d_expenses/1000,
        'total_v_expenses': total_v_expenses/1000,
        'total_g_expenses': total_g_expenses/1000,
        'total_payout': total_payout/1000,
        #
        'total_debit': total_debit/1000,
        'total_credit': total_credit/1000,

        'transactions': transactions,
        'drivers': drivers,
        'vehicles': vehicles,
        'partners': partners,
        'v_revenue': v_revenue,
        # 'd_revenue': d_revenue,

    }
    return render(req, 'finances/accounting/stats.html', context)


# -------------------------------- partner revenues ------------------------------------


@login_required(login_url='login')
def revenues(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    revenues = Revenue.objects.filter(
        Q(partner__last_name__icontains=query)
        | Q(partner__first_name__icontains=query)
        | Q(vehicle__make__icontains=query)
        | Q(vehicle__model__icontains=query)
        | Q(vehicle__plate_number__icontains=query)
    ).order_by('payday')
    context = {
        "finance_page": "active",
        'title': 'vehicle revenues',
        'revenues': revenues,

    }
    return render(req, 'finances/accounting/revenues.html', context)


@login_required(login_url='login')
def revenue(req, pk):
    user = req.user
    curr_revenue = Revenue.objects.get(id=pk)
    rel_revenues = Revenue.objects.filter(
        vehicle=curr_revenue.vehicle).exclude(id=pk)
    context = {
        "finance_page": "active",
        'title': 'driver_revenue',
        'curr_revenue': curr_revenue,
        'rel_revenues': rel_revenues,

    }
    return render(req, 'finances/accounting/revenue.html', context)


@login_required(login_url='login')
def create_revenue(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = RevenueForm()
    if req.method == 'POST':
        form = RevenueForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('revenues')

    context = {
        "finance_page": "active",
        "title": 'create_revenues',
        "form": form,
    }
    return render(req, 'finances/accounting/revenue.html', context)


@login_required(login_url='login')
def edit_revenue(req, pk):
    curr_revenue = Revenue.objects.get(id=pk)
    user = req.user
    if not curr_revenue and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = RevenueForm(instance=curr_revenue)
    if req.method == 'POST':
        form = RevenueForm(req.POST, req.FILES, instance=curr_revenue)
        if form.is_valid():
            form.save()
            return redirect('revenues')

    context = {
        "finance_page": "active",
        "title": 'edit_revenue',
        "form": form,
        "curr_revenue": curr_revenue}
    return render(req, 'finances/accounting/revenue.html', context)


@login_required(login_url='login')
def delete_revenue(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    obj = Revenue.objects.get(id=pk)
    obj.delete()
    return redirect('revenues')


# --------------------------------  vaults CRUD ------------------------------------
@login_required(login_url='login')
def vaults(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    cash_vaults = Vault.objects.filter(type='cash')
    mobile_vaults = Vault.objects.filter(type='mobile')
    bank_vaults = Vault.objects.filter(type='bank')
    context = {
        "vaults_page": "active",
        'title': 'vaults',
        'cash_vaults': cash_vaults,
        'mobile_vaults': mobile_vaults,
        'bank_vaults': bank_vaults,

    }
    return render(req, 'finances/accounting/vaults.html', context)


@login_required(login_url='login')
def vault(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    curr_vault = Vault.objects.get(id=pk)
    rel_ledgers = Ledger.objects.filter(vault=curr_vault)
    vault_balance = curr_vault.credit - curr_vault.debit
    context = {
        "vaults_page": "active",
        'title': 'vault',
        'curr_vault': curr_vault,
        'rel_ledgers': rel_ledgers,
        'vault_balance': vault_balance,

    }
    return render(req, 'finances/accounting/vault.html', context)


@login_required(login_url='login')
def create_vault(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VaultForm()
    if req.method == 'POST':
        form = VaultForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('vaults')

    context = {
        "vaults_page": "active",
        "title": 'create vault',
        "form": form,
    }
    return render(req, 'finances/accounting/vault.html', context)


@login_required(login_url='login')
def edit_vault(req, pk):
    user = req.user
    curr_vault = Vault.objects.get(id=pk)
    if not curr_vault and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VaultForm(instance=curr_vault)
    if req.method == 'POST':
        form = VaultForm(req.POST, instance=curr_vault)
        if form.is_valid():
            form.save()
            return redirect('vaults')

    context = {
        "vaults_page": "active",
        "title": 'edit vault',
        "form": form,
        "curr_vault": curr_vault}
    return render(req, 'finances/accounting/vault.html', context)


@login_required(login_url='login')
def delete_vault(req, pk):
    obj = Vault.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return redirect('vaults')


# --------------------------------  ledgers CRUD ------------------------------------


@login_required(login_url='login')
def ledgers(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    query = req.GET.get('query') if req.GET.get('query') != None else ''
    ledgers = Ledger.objects.filter(
        Q(credit__icontains=query)
        | Q(debit__icontains=query)
        | Q(details__icontains=query)
        | Q(vault__name__icontains=query)
    ).order_by('date')
    context = {
        "finance_page": "active",
        'title': 'vehicle ledgers',
        'ledgers': ledgers,

    }
    return render(req, 'finances/accounting/ledgers.html', context)


@login_required(login_url='login')
def ledger(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    curr_ledger = Ledger.objects.get(id=pk)
    rel_ledgers = Ledger.objects.all().exclude(id=pk)
    context = {
        "finance_page": "active",
        'title': 'driver_ledger',
        'curr_ledger': curr_ledger,
        'rel_ledgers': rel_ledgers,

    }
    return render(req, 'finances/accounting/ledger.html', context)


@login_required(login_url='login')
def create_ledger(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = LedgerForm()
    if req.method == 'POST':
        form = LedgerForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('ledgers')

    context = {
        "finance_page": "active",
        "title": 'create_ledgers',
        "form": form,
    }
    return render(req, 'finances/accounting/ledger.html', context)


@login_required(login_url='login')
def edit_ledger(req, pk):
    user = req.user
    curr_ledger = Ledger.objects.get(id=pk)
    if not curr_ledger and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = LedgerForm(instance=curr_ledger)
    if req.method == 'POST':
        form = LedgerForm(req.POST, instance=curr_ledger)
        if form.is_valid():
            form.save()
            return redirect('ledgers')

    context = {
        "finance_page": "active",
        "title": 'edit_ledger',
        "form": form,
        "curr_ledger": curr_ledger}
    return render(req, 'finances/accounting/ledger.html', context)


@login_required(login_url='login')
def audit_ledger(req, pk):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            obj = Ledger.objects.get(id=pk)
            if obj.is_audited == False:
                Ledger.objects.filter(id=pk).update(is_audited=True)
            else:
                Ledger.objects.filter(id=pk).update(is_audited=False)
        except Ledger.DoesNotExist:
            return HttpResponse('Ledger not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def delete_ledger(req, pk):
    obj = Ledger.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return redirect('ledgers')
