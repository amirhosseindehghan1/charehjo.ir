from django.shortcuts import render, redirect
# from .forms import RegisterForm
# from .models import Register
import random
import string
from django.shortcuts import render, redirect
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

def grade_sheet(request):
    image_list = [
        "/static/images/number1.png",
        "/static/images/number2.png",
        "/static/images/number3blue.png",
        # Add the rest of your image URLs here...
    ]

    # Shuffle the image_list randomly
    random.shuffle(image_list)

    # Determine the number of images per row (let's assume 4 images per row)
    images_per_row = 4

    # Split the image_list into rows
    image_rows = [image_list[i:i + images_per_row] for i in range(0, len(image_list), images_per_row)]


    return render(request, 'grade_sheet.html', {'image_rows': image_rows})

def roadmap(request):
    return render(request, 'roadmap.html')