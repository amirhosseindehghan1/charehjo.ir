from django.shortcuts import render

# Create your views here.

def discovery(request):
    return render(request, 'discovery.html')

def market(request):
    return render(request, 'market.html')

def develop_and_launch(request):
    return render(request, 'develop_and_launch.html')