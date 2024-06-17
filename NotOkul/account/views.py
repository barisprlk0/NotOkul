from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from school.models import SchoolNote

# Create your views here.


def profile(request):

    posts = SchoolNote.objects.filter(author__username=request.user.username)

    context = {'posts': posts}

    return render(request, "school/profile.html", context)


def register_view(request):
    form = RegisterForm(request.POST or None, )
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, user)

        return redirect('home:home')

    return render(request, "account/form.html", {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('home:home')
    return render(request, 'account/form.html', {'form': form})


def logout_view(request):
    logout(request)

    return redirect('home:home')
