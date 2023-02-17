# src/homepage/views.py

from django.shortcuts import render
from .forms import HomePageForm


def home_page(request, *args, **kwargs):
    form = HomePageForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = HomePageForm()

    context = {
        'form': form
    }
    return render(request, 'home.html', context)


