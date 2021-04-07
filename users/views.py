from django.shortcuts import render
from users.models import *
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    return render(request, 'users/dashboard.html')