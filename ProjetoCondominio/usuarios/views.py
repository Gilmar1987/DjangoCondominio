from django.shortcuts import render

# Create your views here.
# usuarios/views.py (ou core/views.py)
from django.shortcuts import render

def home(request):
    return render(request, 'usuarios/home.html')