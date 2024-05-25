import requests as rq
import matplotlib.pyplot as plt


def get_data(city,api_key):
    url=f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=5"
    responce=rq.get(url)
    data=responce.json()
    return data


def plots(data):
    dates=[]
    temperatures=[]
    for forecast in data['forecast']['forecastday']:
        for hour in forecast['hour']:
            dates.append(hour['time'])
            temperatures.append(hour['temp_c'])
    
    
    plt.plot(dates, temperatures,marker='o')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title('Weather Forcast Data')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
        city="bhimavaram"
        api_key='api key'
        data=get_data(city,api_key)
        if 'error' not in data:
            plots(data)
        else:
            print("Error:", data['error']['message'])
        
        
if __name__=="__main__":
    main()
