from django.shortcuts import render
from django.http import JsonResponse
from .llm_engine import get_fire_prediction  # Your custom model

def home(request):
    return render(request, "predictor/index.html")

def simulate(request):
    if request.method == "POST":
        data = request.POST
        lat = data.get("lat")
        lon = data.get("lon")
        temp = data.get("temp")
        wind = data.get("wind")
        humidity = data.get("humidity")

        prediction = get_fire_prediction(lat, lon, temp, wind, humidity)
        return JsonResponse({"prediction": prediction})
