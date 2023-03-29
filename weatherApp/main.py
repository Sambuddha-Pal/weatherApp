import requests
import json
import win32com.client as wincom
city= input("enter the city: ")
url=f"http://api.weatherapi.com/v1/forecast.json?key=283ba3dfe9db44349b873050232903&q={city}&days=1&aqi=no&alerts=no"
r=requests.get(url)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
w1=wdic["current"]["wind_kph"]
w2=wdic["current"]["cloud"]
w3=wdic["current"]["humidity"]
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(f"the temperature of {city} is {w} the wind speed in Kilometers per hour is {w1} cloud is {w2} and humidity is {w3}")
