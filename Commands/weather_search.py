import urllib2
import json

def weather_search(message):
    if len(message.content.split()) == 1:
        return ["City and country/state not given", "message"]
    city_and_country = message[10:].replace(" ", "") 
    imperial_info = json.loads(urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial").format(city_and_country).read())
    city_name = imperial_info["name"]
    city_country = imperial_info["sys"]["country"]
    imperial_temperature = str(imperial_info["main"]["temp"])
    imperial_high = str(imperial_info["main"]["temp_max"])
    imperial_low = str(imperial_info["main"]["temp_min"])
    imperial_condition = [imperial_info["weather"][i]["description"] for i in range(len(imperial_info["weather"]))]

    metric_info = json.loads(urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_state + "&units=metric").read())
    metric_temperature = str(metric_info["main"]["temp"])
    metric_high = str(metric_info["main"]["temp_max"])
    metric_low = str(metric_info["main"]["temp_min"])

    return ["Weather for {0}, {1}\nTemperature: {2} F / {3} C\nHigh: {4} F / {5} C\nLow: {6} F / {7} C\nCurrent Condition: {8}".format(city_name, city_country, imperial_temperature, metric_temperature, imperial_high, metric_high, imperial_low, metric_low, ", ".join(imperial_condition)), "message"]
