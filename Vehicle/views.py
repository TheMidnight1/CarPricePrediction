from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import VehicleValuationForm


def valuation_form(request):

    form = VehicleValuationForm()

    return render(request, 'valuation_form .html', {'form': form})


@login_required
def Form(request):
    form = VehicleValuationForm()
    return render(request, 'valuation_form.html')
