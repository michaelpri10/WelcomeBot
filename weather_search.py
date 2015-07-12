import urllib2
import json


def weather_search(city, country_state):
    print "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_state + "&units=imperial"
    imperial_info = json.loads(urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_state + "&units=imperial").read())
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

    return "Weather for " + city_name + ", " + city_country + "\nTemperature: " + imperial_temperature + " F / " + metric_temperature + " C\nHigh: " + imperial_high + " F / " + metric_high + " C\nLow: " + imperial_low + " F / " + metric_low + " C\nCurrent Condition: " + ", ".join(imperial_condition)
