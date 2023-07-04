from django.urls import path
from .views import *

urlpatterns = [
    path('', finances, name='finances'),
    #
    path('expenses/', expenses, name='expenses'),
    # driver expenses
    path('d_expenses/', d_expenses, name='d_expenses'),
    path('expenses/driver_exp/create', create_d_expense, name='create_d_expense'),
    path('expenses/driver_exp/<str:pk>/', d_expense, name='d_expense'),
    path('expenses/driver_exp/<str:pk>/edit',
         edit_d_expense, name='edit_d_expense'),
    path('expenses/driver_exp/<str:pk>/delete',
         delete_d_expense, name='delete_d_expense'),
    # vehicle expenses
    path('v_expenses/', v_expenses, name='v_expenses'),
    path('expenses/vehicle_exp/create',
         create_v_expense, name='create_v_expense'),
    path('expenses/vehicle_exp/<str:pk>/', v_expense, name='v_expense'),
    path('expenses/vehicle_exp/<str:pk>/edit',
         edit_v_expense, name='edit_v_expense'),
    path('expenses/vehicle_exp/<str:pk>/delete',
         delete_v_expense, name='delete_v_expense'),
    # global expenses
    path('g_expenses/', g_expenses, name='g_expenses'),
    path('expenses/global_exp/create', create_g_expense, name='create_g_expense'),
    path('expenses/global_exp/<str:pk>/', g_expense, name='g_expense'),
    path('expenses/global_exp/<str:pk>/edit',
         edit_g_expense, name='edit_g_expense'),
    path('expenses/global_exp/<str:pk>/delete',
         delete_g_expense, name='delete_g_expense'),
    # transactions
    path('transactions/', transactions, name='transactions'),
    # payments
    path('payments/', payments, name='payments'),
    path('payments/create', create_payment, name='create_payment'),
    path('payments/<str:pk>/', payment, name='payment'),
    path('payments/<str:pk>/edit', edit_payment, name='edit_payment'),
    path('payments/<str:pk>/delete', delete_payment, name='delete_payment'),
    # payouts
    path('payouts/', payouts, name='payouts'),
    path('payouts/create', create_payout, name='create_payout'),
    path('payouts/<str:pk>/', payout, name='payout'),
    path('payouts/<str:pk>/edit', edit_payout, name='edit_payout'),
    path('payouts/<str:pk>/delete', delete_payout, name='delete_payout'),
    # ledgers
    path('ledgers/', ledgers, name='ledgers'),
    path('ledgers/create', create_ledger, name='create_ledger'),
    path('ledgers/<str:pk>/', ledger, name='ledger'),
    path('ledgers/<str:pk>/edit', edit_ledger, name='edit_ledger'),
    path('ledgers/<str:pk>/delete', delete_ledger, name='delete_ledger'),
    # dividends
    path('dividends/', dividends, name='dividends'),
    path('dividends/create', create_dividend, name='create_dividend'),
    path('dividends/<str:pk>/', dividend, name='dividend'),
    path('dividends/<str:pk>/edit', edit_dividend, name='edit_dividend'),
    path('dividends/<str:pk>/delete', delete_dividend, name='delete_dividend'),
    # balancesheet & audit
    path('balancesheet/', balancesheet, name='balancesheet'),
    path('audit/', audit, name='audit'),
]
