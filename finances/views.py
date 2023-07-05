from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Min, Max

# from finances.forms import LedgerForm

from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.


@login_required(login_url='login')
def finances(req):
    user = req.user
    d_expenses = DriverExpense.objects.filter().count()
    v_expenses = VehicleExpense.objects.all().count()
    g_expenses = GlobalExpense.objects.all().count()
    payments = Payment.objects.all().count()
    payouts = Payout.objects.all().count()
    transactions = payments+payouts

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
    users = CustomUser.objects.all()
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    d_expenses = DriverExpense.objects.all().order_by('date_posted')
    v_expenses = VehicleExpense.objects.all().order_by('date_posted')
    g_expenses = GlobalExpense.objects.all().order_by('date_posted')

    context = {
        "expenses_page": "active",
        'title': 'expenses',
        'users': users,
        'd_expenses': d_expenses,
        'v_expenses': v_expenses,
        'g_expenses': g_expenses,

    }
    return render(req, 'finances/expenses/index.html', context)


# -------------------------------- driver expenses ------------------------------------


@login_required(login_url='login')
def d_expenses(req):
    user = req.user
    users = CustomUser.objects.all()
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    d_expenses = DriverExpense.objects.filter(
        Q(amount__icontains=query)
        | Q(details__icontains=query)
        | Q(driver__first_name__icontains=query)
        | Q(driver__last_name__icontains=query)
    ).order_by('date_posted')

    context = {
        "expenses_page": "active",
        'title': 'expenses',
        'users': users,
        'd_expenses': d_expenses,

    }
    return render(req, 'finances/expenses/d_expenses.html', context)


@login_required(login_url='login')
def d_expense(req, pk):
    user = req.user
    curr_expense = DriverExpense.objects.get(id=pk)
    rel_expenses = DriverExpense.objects.filter(
        driver=curr_expense.driver).exclude(id=pk)
    context = {
        "expense_page": "active",
        'title': 'driver expense',
        'curr_expense': curr_expense,
        'rel_expenses': rel_expenses,

    }
    return render(req, 'finances/expenses/d_expense.html', context)


@login_required(login_url='login')
def create_d_expense(req):
    user = req.user
    # if user.role.sec_level == 2:
    #     return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DriverExpenseForm()
    if req.method == 'POST':
        form = DriverExpenseForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "create_d_expense_page": "active",
        "title": 'create driver expenses',
        "form": form,
    }
    return render(req, 'finances/expenses/d_expense.html', context)


@login_required(login_url='login')
def edit_d_expense(req, pk):
    user = req.user
    curr_expense = DriverExpense.objects.get(id=pk)
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DriverExpenseForm(instance=curr_expense)
    if req.method == 'POST':
        form = DriverExpenseForm(req.POST, instance=curr_expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "edit_d_expense_page": "active",
        "title": 'edit driver expenses',
        "form": form,
        "curr_expense": curr_expense}
    return render(req, 'finances/expenses/d_expense.html', context)


@login_required(login_url='login')
def delete_d_expense(req, pk):
    doc = DriverExpense.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    doc.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# -------------------------------- vehicle expenses ------------------------------------

@login_required(login_url='login')
def v_expenses(req):
    user = req.user
    users = CustomUser.objects.all()
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    v_expenses = VehicleExpense.objects.filter(
        Q(amount__icontains=query)
        | Q(details__icontains=query)
        | Q(vehicle__model__icontains=query)
        | Q(vehicle__make__icontains=query)
    ).order_by('date_posted')

    context = {
        "expenses_page": "active",
        'title': 'expenses',
        'users': users,
        'v_expenses': v_expenses,

    }
    return render(req, 'finances/expenses/v_expenses.html', context)


@login_required(login_url='login')
def v_expense(req, pk):
    user = req.user
    curr_expense = VehicleExpense.objects.get(id=pk)
    rel_expenses = VehicleExpense.objects.filter(
        vehicle=curr_expense.vehicle).exclude(id=pk)
    context = {
        "expense_page": "active",
        'title': 'driver_expense',
        'curr_expense': curr_expense,
        'rel_expenses': rel_expenses,

    }
    return render(req, 'finances/expenses/v_expense.html', context)


@login_required(login_url='login')
def create_v_expense(req):
    user = req.user
    # if user.role.sec_level == 2:
    #     return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VehicleExpenseForm()
    if req.method == 'POST':
        form = VehicleExpenseForm(req.POST)
        # print(form.instance)
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "create_v_expense_page": "active",
        "title": 'create vehicle expenses',
        "form": form,
    }
    return render(req, 'finances/expenses/v_expense.html', context)


@login_required(login_url='login')
def edit_v_expense(req, pk):
    user = req.user
    curr_expense = VehicleExpense.objects.get(id=pk)
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = VehicleExpenseForm(instance=curr_expense)
    if req.method == 'POST':
        form = VehicleExpenseForm(req.POST, instance=curr_expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "edit_v_expense_page": "active",
        "title": 'edit vehicle expenses',
        "form": form,
        "curr_expense": curr_expense}
    return render(req, 'finances/expenses/v_expense.html', context)


@login_required(login_url='login')
def delete_v_expense(req, pk):
    doc = VehicleExpense.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    doc.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# -------------------------------- global expenses ------------------------------------


@login_required(login_url='login')
def g_expenses(req):
    user = req.user
    users = CustomUser.objects.all()
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    g_expenses = GlobalExpense.objects.filter(
        Q(amount__icontains=query)
        | Q(details__icontains=query)
        | Q(author__first_name__icontains=query)
        | Q(author__last_name__icontains=query)
    ).order_by('date_posted')

    context = {
        "expenses_page": "active",
        'title': 'expenses',
        'users': users,
        'g_expenses': g_expenses,

    }
    return render(req, 'finances/expenses/g_expenses.html', context)


@login_required(login_url='login')
def g_expense(req, pk):
    user = req.user
    curr_expense = GlobalExpense.objects.get(id=pk)
    rel_expenses = GlobalExpense.objects.filter(
        author=curr_expense.author).exclude(id=pk)
    context = {
        "expense_page": "active",
        'title': 'driver expense',
        'curr_expense': curr_expense,
        'rel_expenses': rel_expenses,

    }
    return render(req, 'finances/expenses/g_expense.html', context)


@login_required(login_url='login')
def create_g_expense(req):
    user = req.user
    # if user.role.sec_level == 2:
    #     return redirect(req.META.get('HTTP_REFERER', '/'))

    form = GlobalExpenseForm()
    if req.method == 'POST':
        form = GlobalExpenseForm(req.POST)
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "create_g_expense_page": "active",
        "title": 'create global expenses',
        "form": form,
    }
    return render(req, 'finances/expenses/g_expense.html', context)


@login_required(login_url='login')
def edit_g_expense(req, pk):
    user = req.user
    curr_expense = GlobalExpense.objects.get(id=pk)
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = GlobalExpenseForm(instance=curr_expense)
    if req.method == 'POST':
        form = GlobalExpenseForm(req.POST, instance=curr_expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')

    context = {
        "edit_g_expense_page": "active",
        "title": 'edit global expenses',
        "form": form,
        "curr_expense": curr_expense}
    return render(req, 'finances/expenses/g_expense.html', context)


@login_required(login_url='login')
def delete_g_expense(req, pk):
    doc = GlobalExpense.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    doc.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

# --------------------------------------------------------- transactions CRUD ---------------------------------------------------------


@login_required(login_url='login')
def transactions(req):
    user = req.user
    payments = Payment.objects.all()
    payouts = Payout.objects.all()
    context = {
        "transactions_page": "active",
        'title': 'transactions',
        'payments': payments,
        'payouts': payouts,

    }
    return render(req, 'finances/transactions/index.html', context)


# -------------------------------- driver payments ------------------------------------


@login_required(login_url='login')
def payments(req):
    user = req.user
    payments = Payment.objects.all()
    print('Payments page', payments)
    context = {
        "payments_page": "active",
        'title': 'payments',
        'payments': payments,

    }
    return render(req, 'finances/transactions/payments.html', context)


@login_required(login_url='login')
def payment(req, pk):
    user = req.user
    curr_payment = Payment.objects.get(id=pk)
    rel_payments = Payment.objects.filter(
        driver=curr_payment.driver).exclude(id=pk)
    context = {
        "payment_page": "active",
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
        form = PaymentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('payments')

    context = {
        "create_payment_page": "active",
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
        form = PaymentForm(req.POST, instance=curr_payment)
        if form.is_valid():
            form.save()
            return redirect('payments')

    context = {
        "edit_payment_page": "active",
        "title": 'edit_payment',
        "form": form,
        "curr_payment": curr_payment}
    return render(req, 'finances/transactions/payment.html', context)


@login_required(login_url='login')
def delete_payment(req, pk):
    doc = Payment.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    doc.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# -------------------------------- driver payouts ------------------------------------


@login_required(login_url='login')
def payouts(req):
    user = req.user
    payouts = Payout.objects.all()
    context = {
        "payouts_page": "active",
        'title': 'driver payouts',
        'payouts': payouts,

    }
    return render(req, 'finances/transactions/payouts.html', context)


@login_required(login_url='login')
def payout(req, pk):
    user = req.user
    curr_payout = Payout.objects.get(id=pk)
    rel_payouts = Payout.objects.filter(
        driver=curr_payout.driver).exclude(id=pk)
    context = {
        "payout_page": "active",
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
        form = PayoutForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('payouts')

    context = {
        "create_payout_page": "active",
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
        form = PayoutForm(req.POST, instance=curr_payout)
        if form.is_valid():
            form.save()
            return redirect('payouts')

    context = {
        "edit_payout_page": "active",
        "title": 'edit_payout',
        "form": form,
        "curr_payout": curr_payout}
    return render(req, 'finances/transactions/payout.html', context)


@login_required(login_url='login')
def delete_payout(req, pk):
    doc = Payout.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    doc.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

# --------------------------------------------------------- bookkeeping CRUD ---------------------------------------------------------

# -------------------------------- vehicle ledgers ------------------------------------


@login_required(login_url='login')
def ledgers(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    ledgers = Ledger.objects.filter(
        Q(credit__icontains=query)
        | Q(debit__icontains=query)
        | Q(vehicle__make__icontains=query)
        | Q(vehicle__model__icontains=query)
        | Q(vehicle__plate_number__icontains=query)
    ).order_by('date')
    context = {
        "ledgers_page": "active",
        'title': 'vehicle ledgers',
        'ledgers': ledgers,

    }
    return render(req, 'finances/accounting/ledgers.html', context)


@login_required(login_url='login')
def ledger(req, pk):
    user = req.user
    curr_ledger = Ledger.objects.get(id=pk)
    rel_ledgers = Ledger.objects.filter(
        vehicle=curr_ledger.vehicle).exclude(id=pk)
    context = {
        "ledger_page": "active",
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
        "create_ledger_page": "active",
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
        "edit_ledger_page": "active",
        "title": 'edit_ledger',
        "form": form,
        "curr_ledger": curr_ledger}
    return render(req, 'finances/accounting/ledger.html', context)


@login_required(login_url='login')
def delete_ledger(req, pk):
    doc = Ledger.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    doc.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# -------------------------------- balancesheet & audits ------------------------------------


@login_required(login_url='login')
def balancesheet(req):
    user = req.user
    ledgers = Ledger.objects.all().count()
    payments = Payment.objects.all().count()
    payouts = Payout.objects.all().count()
    d_expenses = DriverExpense.objects.filter().count()
    v_expenses = VehicleExpense.objects.all().count()
    g_expenses = GlobalExpense.objects.all().count()

    # --------------------------------------------------------credit / payments--------------------------------------------------------
    total_payment = Payment.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_payment = Payment.objects.all().aggregate(Max('amount'))[
        'amount__max'] or 0
    min_payment = Payment.objects.all().aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_payment = Payment.objects.all().aggregate(Avg('amount'))[
        'amount__avg'] or 0

    # --------------------------------------------------------debit--------------------------------------------------------
    
    # payouts--------------------------------------------------------
    total_payout = Payout.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_payout = Payout.objects.all().aggregate(Max('amount'))[
        'amount__max'] or 0
    min_payout = Payout.objects.all().aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_payout = Payout.objects.all().aggregate(Avg('amount'))[
        'amount__avg'] or 0
    
    # expenses--------------------------------------------------------
    total_d_exp = DriverExpense.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_d_exp = DriverExpense.objects.all().aggregate(Max('amount'))[
        'amount__max'] or 0
    min_d_exp = DriverExpense.objects.all().aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_d_exp = DriverExpense.objects.all().aggregate(Avg('amount'))[
        'amount__avg'] or 0
    
    total_v_exp = VehicleExpense.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_v_exp = VehicleExpense.objects.all().aggregate(Max('amount'))[
        'amount__max'] or 0
    min_v_exp = VehicleExpense.objects.all().aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_v_exp = VehicleExpense.objects.all().aggregate(Avg('amount'))[
        'amount__avg'] or 0
    
    total_g_exp = GlobalExpense.objects.all().aggregate(Sum('amount'))[
        'amount__sum'] or 0
    max_g_exp = GlobalExpense.objects.all().aggregate(Max('amount'))[
        'amount__max'] or 0
    min_g_exp = GlobalExpense.objects.all().aggregate(Min('amount'))[
        'amount__min'] or 0
    avg_g_exp = GlobalExpense.objects.all().aggregate(Avg('amount'))[
        'amount__avg'] or 0

    # balance
    total_credit = total_payout
    total_debit = total_payout + total_d_exp + total_v_exp + total_g_exp
    total_balance = total_credit - total_debit

    context = {
        "balancesheet_page": "active",
        'title': 'company balancesheet',
        'ledgers': ledgers,
        'payments': payments,
        'payouts': payouts,
        'd_expenses': d_expenses,
        'v_expenses': v_expenses,
        'g_expenses': g_expenses,

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
        'total_d_expenses ': total_d_exp,
        'max_d_expenses': max_d_exp,
        'min_d_expenses': min_d_exp,
        'avg_d_expenses': avg_d_exp,

        # v_expenses
        'total_v_expenses ': total_v_exp,
        'max_v_expenses': max_v_exp,
        'min_v_expenses': min_v_exp,
        'avg_v_expenses': avg_v_exp,

        # g_expenses
        'total_g_expenses ': total_g_exp,
        'max_g_expenses': max_g_exp,
        'min_g__expenses': min_g_exp,
        'avg_g__expenses': avg_g_exp,
        
        # balance
        'total_credit': total_credit,
        'total_debit': total_debit,
        'total_balance': total_balance,

    }
    return render(req, 'finances/accounting/balancesheet.html', context)


@login_required(login_url='login')
def audit(req):
    user = req.user
    payments = Payment.objects.all().all().order_by('-date_paid')
    payouts = Payout.objects.all().all().order_by('-date_paid')
    d_expenses = DriverExpense.objects.all().order_by('-date_posted')
    v_expenses = VehicleExpense.objects.all().order_by('-date_posted')
    g_expenses = GlobalExpense.objects.all().order_by('-date_posted')
    context = {
        "audit_page": "active",
        'title': 'audits',
        'payments': payments,
        'payouts': payouts,
        'd_expenses': d_expenses,
        'v_expenses': v_expenses,
        'g_expenses': g_expenses,

    }
    return render(req, 'finances/accounting/audit.html', context)


# -------------------------------- partner dividends ------------------------------------


@login_required(login_url='login')
def dividends(req):
    user = req.user
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    dividends = Dividend.objects.filter(
        Q(partner__last_name__icontains=query)
        | Q(partner__first_name__icontains=query)
        | Q(vehicle__make__icontains=query)
        | Q(vehicle__model__icontains=query)
        | Q(vehicle__plate_number__icontains=query)
    ).order_by('date_paid')
    context = {
        "dividends_page": "active",
        'title': 'vehicle dividends',
        'dividends': dividends,

    }
    return render(req, 'finances/accounting/dividends.html', context)


@login_required(login_url='login')
def dividend(req, pk):
    user = req.user
    curr_dividend = Dividend.objects.get(id=pk)
    rel_dividends = Dividend.objects.filter(
        vehicle=curr_dividend.vehicle).exclude(id=pk)
    context = {
        "dividend_page": "active",
        'title': 'driver_dividend',
        'curr_dividend': curr_dividend,
        'rel_dividends': rel_dividends,

    }
    return render(req, 'finances/accounting/dividend.html', context)


@login_required(login_url='login')
def create_dividend(req):
    user = req.user
    if user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DividendForm()
    if req.method == 'POST':
        form = DividendForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('dividends')

    context = {
        "create_dividend_page": "active",
        "title": 'create_dividends',
        "form": form,
    }
    return render(req, 'finances/accounting/dividend.html', context)


@login_required(login_url='login')
def edit_dividend(req, pk):
    user = req.user
    curr_dividend = Dividend.objects.get(id=pk)
    if not curr_dividend and user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = DividendForm(instance=curr_dividend)
    if req.method == 'POST':
        form = DividendForm(req.POST, instance=curr_dividend)
        if form.is_valid():
            form.save()
            return redirect('dividends')

    context = {
        "edit_dividend_page": "active",
        "title": 'edit_dividend',
        "form": form,
        "curr_dividend": curr_dividend}
    return render(req, 'finances/accounting/dividend.html', context)


@login_required(login_url='login')
def delete_dividend(req, pk):
    doc = Dividend.objects.get(id=pk)
    if req.user.role.sec_level < 3:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    doc.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
