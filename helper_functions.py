import os
from dotenv import load_dotenv
import requests

# load api_key
load_dotenv()
api_key = os.getenv("api_key")

def get_api_key()-> object:
    """
    get api parameters

    :return: parameter object for http request including api key, city information and days
    """ 
    return {"key": api_key, "q":"Mannheim", "days":1}

def get_raw_forecast()-> None:
    response = requests.get("http://api.weatherapi.com/v1/forecast.json", params=get_api_key())

    if response.status_code == 200:
        return response.json()
    
    else:
        print("Error:", response.status_code)


def get_forecast_day()-> object:
    """
    gets forecast of today
    :return: weather forecast of today including metrics such as min and max temperatures, chance of snow/rain, etc. 
    """
    return get_raw_forecast()["forecast"]["forecastday"][0]["day"]

if __name__ == "__main__":
    pass