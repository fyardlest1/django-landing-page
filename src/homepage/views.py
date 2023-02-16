# fyardhome/homepage/views.py

from django.shortcuts import render

def home_page(request, *args, **kwargs):
    return render(request, 'home.html')


