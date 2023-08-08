from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# from .forms import RegisterForm
# from .models import Register
from django.contrib import messages
import random
import string
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate

from . import forms
from .forms import RegistrationForm
# Create your views here.

def discovery(request):
    return render(request, 'discovery.html')

def market(request):
    return render(request, 'market.html')

def develop_and_launch(request):
    return render(request, 'develop_and_launch.html')

def problem_solving(request):
    return render(request, 'problem_solving.html')

def generate_random_password():
    # Generate a random password using uppercase letters, lowercase letters, and digits
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(10))
    return password


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user without committing to the database
            user = form.save(commit=False)

            # Generate a random password
            password = generate_random_password()
            user.set_password(password)


            # Save the user object with the random password
            user.save()

            # Auto-login the user after successful registration
            user = authenticate(request, email=user.email, password=password)
            login(request, user)

            return redirect('/grade-sheet')  # Change 'home' to the URL name of your homepage
    else:
        form = RegistrationForm()
        # Remove the password field from the form so it won't be displayed
        form.fields.pop('password', None)
        # Set a random password to be sent along with the form data
        form.initial['password'] = generate_random_password()
    return render(request, 'register.html', {'form': form})
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/grade-sheet')
    # else:
    #     form = RegisterForm()

    # return render(request, 'register.html')


@login_required(login_url='/admin/')
def grade_sheet(request):

    return render(request, 'grade_sheet.html')


@login_required(login_url='/')
def roadmap(request):
    if request.method == 'POST':
        user = request.user
        if 'free_button' in request.POST:
            user.free = True
            messages.success(request, "به زودی ایمیلی حاوی لینک ثبت نام و درگاه پرداخت برای شما ارسال خواهد شد.")

        if 'moghadamati_button' in request.POST:
            user.moghadamati = True
            messages.success(request, "به زودی ایمیلی حاوی لینک ثبت نام و درگاه پرداخت برای شما ارسال خواهد شد.")

        if 'takmili_button' in request.POST:
            user.takmili = True
            messages.success(request, "به زودی ایمیلی حاوی لینک ثبت نام و درگاه پرداخت برای شما ارسال خواهد شد.")

        if 'pro_button' in request.POST:
            user.pro = True
            messages.success(request, "به زودی ایمیلی حاوی لینک ثبت نام و درگاه پرداخت برای شما ارسال خواهد شد.")

        user.save()

        return HttpResponseRedirect(reverse('roadmap'))

    return render(request, 'roadmap.html')