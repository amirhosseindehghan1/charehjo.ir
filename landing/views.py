from django.shortcuts import render

# Create your views here.

def discovery(request):
    return render(request, 'discovery.html')

def market(request):
    return render(request, 'market.html')