from django.shortcuts import render
import joblib
import numpy as np
import os
from django.conf import settings
# model = joblib.load('ml/house_price_model.pkl')
# Create your views here.

# Safe model load using try-except
model = None
model_path = os.path.join(settings.BASE_DIR, 'ml', 'house_price_model.pkl')
if os.path.exists(model_path):
    try:
        model = joblib.load(model_path)
    except Exception as e:
        print(f"❌ Error loading model: {e}")
else:
    print("❌ Model file not found at:", model_path)


def predict_price(request):
    prediction = None
    error = None
    area = bedrooms = age = None  # Initialize values

    if request.method == "POST":
        if model is None:
            error = "Model is not loaded. Please contact admin."
        else:
            try:
                area = float(request.POST['area'])
                bedrooms = int(request.POST['bedrooms'])
                age = int(request.POST['age'])
                features = np.array([[area, bedrooms, age]])
                prediction = model.predict(features)[0]
            except Exception as e:
                error = f"Invalid input or prediction error: {e}"

    return render(request, 'predictor/form.html', {
        'prediction': prediction,
        'error': error,
        # 'area': area,
        # 'bedrooms': bedrooms,
        # 'age': age
        'area': area if 'area' in locals() else None,
        'bedrooms': bedrooms if 'bedrooms' in locals() else None,
        'age': age if 'age' in locals() else None,
    })