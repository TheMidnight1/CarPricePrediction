import pickle
import pandas as pd
from django.shortcuts import render
from Vehicle.forms import VehicleValuationForm
from django.http import HttpResponse, JsonResponse

# Load the trained model
with open("prediction_model.pkl", "rb") as f:
    model = pickle.load(f)


def prediction(request):
    context = {}  # Initialize the context variable

    if request.method == "POST":
        form = VehicleValuationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["vehicle_name"]
            company = form.cleaned_data["vehicle_brand"]
            year = form.cleaned_data["Year"]
            kms_driven = form.cleaned_data["Distance_Travelled"]
            fuel_type = form.cleaned_data["Fuel"]

            # Create a pandas DataFrame from the form data
            # data = {
            #     'name': [name],
            #     'company': [company],
            #     'year': [year],
            #     'kms_driven': [kms_driven],
            #     'fuel_type': [fuel_type]
            # }
            data = pd.DataFrame(
                [[name, company, year, kms_driven, fuel_type]],
                columns=["name", "company", "year", "kms_driven", "fuel_type"],
            )

            # Make predictions using the trained model
            print("starting prediction")
            prediction = model.predict(data)[0]
            price = prediction if prediction > 0 else 0

            print("prediction done")

            # Update the context dictionary with predictions
            # context["predictions"] = predictions.tolist()

    # Render the template with the context
    # return render(request, 'valuation_form.html', context)
    return JsonResponse({"price": price})
