from datetime import date
import os
import json
import pandas as pd

json_path = "C:/Users/Dell/Desktop/KRISHNA_WORK/python/projects/SimpleWeatherLogSystem/file.json" 
if os.path.exists(json_path):
    if os.stat(json_path).st_size == 0:
        weather = {}
    else:
        with open(json_path,"r+") as f:
            weather = json.load(f)
else:
    with open(json_path,"x") as f:
        weather = {}


date_today = str(date.today())
temperature = {}
for i in ['12am','3am','6am','9am','12pm','3pm','6pm','9pm']:
    try:
        temp = int(input(f"Enter the temperature at {i}: "))
    except ValueError:
        temp = 0
    temperature[i] = temp

def get_todays_temp_details():
    return list(temperature.values())

def get_average_temp():
    return sum(get_todays_temp_details())/8

def get_max_temp():
    return max(get_todays_temp_details())

def get_min_temp():
    return min(get_todays_temp_details())
        
    
with open(json_path,"w") as file:
    weather[date_today] = { "Average": get_average_temp(),
                           "Min_Temp": get_min_temp(),
                           "Max_Temp" : get_max_temp()
    }
    print(pd.DataFrame(weather))
    file.seek(0)
    json.dump(weather,file,indent=4)
    file.truncate()


