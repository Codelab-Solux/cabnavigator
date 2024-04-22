from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
# Create your views here.


def signupView(req):
    if req.user.is_authenticated:
        return redirect('home')

    form = SignupForm()
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "Votre compte vien d'être créé.")
            return redirect('login')
    else:
        form = SignupForm()
    context = {
        "signup_page": "active",
        "title": 'signup',
        'form': form,
    }
    return render(req, 'accounts/signup.html', context)


def loginView(req):
    if req.user.is_authenticated:
        return redirect('home')

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            if 'next' in req.POST:
                return redirect(req.POST.get('next'))

            else:
                return redirect('home')
        else:
            messages.info(req, 'Username or Password is incorrect!')
    context = {
        "login_page": "active",
        "title": 'login'}
    return render(req, 'accounts/login.html', context)


@login_required(login_url='login')
def logoutUser(req):
    logout(req)
    return redirect('login')


@login_required(login_url='login')
def create_user(req):

    if req.user.role.sec_level >= 3:
        form = CreateUserForm()
        if req.method == 'POST':
            form = CreateUserForm(req.POST)
            if form.is_valid():
                form.save()
                messages.success(req, "Le nouveau compte vien d'être créé.")
                return redirect('users')
        else:
            form = CreateUserForm()
    else:
        form = None
    context = {
        "create_user_page": "active",
        'title': 'create_user',
        'form': form,
    }
    return render(req, 'accounts/user.html', context)


@login_required(login_url='login')
def users(req):
    if req.user.role.sec_level < 4:
        return redirect(req.META.get('HTTP_REFERER'))

    users = CustomUser.objects.all()
    ordering = ['last_name']
    context = {
        "users_page": "active",
        'title': 'users',
        'users': users,
        'ordering': ordering,
    }
    return render(req, 'accounts/users.html', context)


@ login_required(login_url='login')
def user_profile(req, pk):
    user = req.user
    profile = CustomUser.objects.get(id=pk)

    if user == profile:
        form = EditUserForm(instance=profile)
        if req.method == 'POST':
            form = EditUserForm(req.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('users')

    elif user.role.sec_level >= 4:
        form = AdminEditUserForm(instance=profile)
        if req.method == 'POST':
            form = AdminEditUserForm(req.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('users')
    else:
        form = None

    context = {
        "profile_page": "active",
        'title': 'user_profile',
        'profile': profile,
        'form': form,
    }
    return render(req, 'accounts/user.html', context)


@login_required(login_url='login')
def delete_user(req, pk):
    if req.user.role.sec_level < 3:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    else:
        user = CustomUser.objects.filter(id=pk)
        if not user:
            return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
        user.delete()
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

#  roles -----------------------------------------------------------------------


@login_required(login_url='login')
def roles(req):
    if not req.user.is_superuser:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = RoleForm()
    if req.method == 'POST':
        form = RoleForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "um nouveau role vien d'être créé.")
            return redirect('roles')

    context = {
        "roles_page": "active",
        'title': 'roles',
        'form': form,
    }
    return render(req, 'accounts/roles.html', context)


@login_required(login_url='login')
def create_role(req):
    if not req.user.is_superuser:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = RoleForm()
    if req.method == 'POST':
        form = RoleForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "um nouveau role vien d'être créé.")
            return redirect('roles')

    context = {
        "create_role_page": "active",
        'title': 'create role',
        'form': form,
    }
    return render(req, 'accounts/role.html', context)


def filter_users(req):
    user_role = req.POST.get('user_role')
    user_phone = req.POST.get('user_phone')
    last_name = req.POST.get('last_name')
    first_name = req.POST.get('first_name')
    user_status = req.POST.get('user_status')
    user_sex = req.POST.get('user_sex')
    user_presence = req.POST.get('user_presence')

    # Construct the base query
    base_query = CustomUser.objects.all().order_by('-last_name')

    # Apply filters based on parameters
    if user_role:
        base_query = base_query.filter(role_id=user_role)
    if user_phone:
        base_query = base_query.filter(phone=user_phone)
    if last_name:
        base_query = base_query.filter(last_name__icontains=last_name)
    if first_name:
        base_query = base_query.filter(first_name__icontains=first_name)
    if user_status:
        base_query = base_query.filter(profile__status__id=user_status)
    if user_sex:
        base_query = base_query.filter(profile__sex=user_sex)
    if user_presence:
        base_query = base_query.filter(
            profile__is_onsite=user_presence.title())

    users = base_query
    context = {"users": users}
    return render(req, 'accounts/partials/users_list.html', context)
