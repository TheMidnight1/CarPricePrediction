from django.contrib import admin
from django.urls import path, include
from .views import MyRegisterView, Homepage, MyLoginView, Aboutus, Services, MyLogoutView, Valuation, FAQ


app_name = 'useraccount'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),

    path('signup/', MyRegisterView.as_view(), name='signup'),
    path('', Homepage, name='homepage'),
    path('aboutus/', Aboutus, name='aboutus'),
    path('services/', Services, name='services'),
    path('valuation_form/', Valuation, name='valuation_form'),
    path('FAQ/', FAQ, name='FAQ'),

]
