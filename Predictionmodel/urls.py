from django.urls import path
from .views import prediction

app_name = "Predictionmodel"
urlpatterns = [
    # Add your specific URL pattern
    path("prediction/", prediction, name="prediction"),
]
