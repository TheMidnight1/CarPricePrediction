from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from . forms import UserForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.


# def LoginPage(request):
#     form = AuthenticationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'Login.html', context)


# def SignupPage(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login/')
#     else:
#         form = UserForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'Signup.html', context)

class MyRegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = "Signup.html"
    success_url = reverse_lazy("useraccount:login")


class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"


class MyLogoutView(LogoutView):

    next_page = reverse_lazy("useraccount:homepage")


def Homepage(request):
    return render(request, 'index.html')


def Aboutus(request):
    return render(request, 'aboutus.html')


def Services(request):
    return render(request, 'services.html')


def Valuation(request):
    return render(request, 'valuation_form.html')

def FAQ(request):
    return render(request, 'FAQ.html')


# def vehicle_valuation(request):
#     if request.method == 'POST':
#         form = VehicleValuationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, '/success/')
#     else:
#         form = VehicleValuationForm()

#     return render(request, 'valuation/form.html', {'form': form})
