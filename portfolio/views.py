from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio

def home(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/home.html', {'portfolios': portfolios})
