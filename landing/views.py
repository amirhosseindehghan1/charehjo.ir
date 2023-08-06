from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Register
# Create your views here.

def discovery(request):
    return render(request, 'discovery.html')

def market(request):
    return render(request, 'market.html')

def develop_and_launch(request):
    return render(request, 'develop_and_launch.html')

def problem_solving(request):
    return render(request, 'problem_solving.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/grade-sheet')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def grade_sheet(request):
    return render(request, 'grade_sheet.html')

def roadmap(request):
    return render(request, 'roadmap.html')