from django.shortcuts import render

# Create your views here.

def discovery(request):
    return render(request, 'discovery.html')

