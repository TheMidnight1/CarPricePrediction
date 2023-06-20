from django.contrib import admin
from django.urls import path, include
from .views import Form
from Vehicle.views import valuation_form



app_name = 'Vehicle'
urlpatterns = [

    path('form/', Form, name='form'),
    path('admin/', admin.site.urls),
    path('valuation/', valuation_form, name='valuation_form'),
    
]
