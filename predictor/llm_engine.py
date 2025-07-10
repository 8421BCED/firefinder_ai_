def get_fire_prediction(lat, lon, temp, wind, humidity):
    # Later call Mistral here via OpenRouter API
    return f"🔥 Fire likely to spread NE from ({lat}, {lon}) due to wind at {wind}km/h and temp {temp}°C."
