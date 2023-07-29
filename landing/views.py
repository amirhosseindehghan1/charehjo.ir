from django.shortcuts import render

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
    return render(request, 'register.html')