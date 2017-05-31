import requests

from weather_source import WeatherSource
from weather_ds import Weather

class SKPWeather(WeatherSource):
    def __init__(self, params):
        super(SKPWeather, self).__init__(params)
        self.appkey = params['appkey']
        self.lat = params['lat']
        self.lon = params['lon']
    
    def get_curr_weather(self):
        url1 = "http://apis.skplanetx.com/weather/current/hourly?version=1&lat=%s&lon=%s" % (self.lat, self.lon)
        r1 = requests.get(url1, headers={'appKey': self.appkey})
        d1 = r1.json()
        url2 = "http://apis.skplanetx.com/weather/dust?version=1&lat=%s&lon=%s" % (self.lat, self.lon)
        r2 = requests.get(url2, headers={'appKey': self.appkey})
        d2 = r2.json()

        return Weather(d1['weather']['hourly'][0]['timeRelease'],
                       d1['weather']['hourly'][0]['sky']['code'],
                       d1['weather']['hourly'][0]['sky']['name'],
                       None,
                       d1['weather']['hourly'][0]['temperature']['tc'],
                       d1['weather']['hourly'][0]['temperature']['tmin'],
                       d1['weather']['hourly'][0]['temperature']['tmax'],
                       d1['weather']['hourly'][0]['humidity'],
                       d2['weather']['dust'][0]['pm10']['grade'],
                       None)

    
    def get_weather_forecast(self):
        url = "http://apis.skplanetx.com/weather/forecast/6days?version=1&lat=%s&lon=%s" % (self.lat, self.lon)
        r = requests.get(url, headers={'appKey': self.appkey})
        d = r.json()
        return [
            Weather(d['weather']['forecast6days'][0]['timeRelease'],
                    d['weather']['forecast6days'][0]['sky']['pmCode2day'],
                    d['weather']['forecast6days'][0]['sky']['pmName2day'],
                    None,
                    None,
                    d['weather']['forecast6days'][0]['temperature']['tmin2day'],
                    d['weather']['forecast6days'][0]['temperature']['tmax2day'],
                    None,
                    None,
                    None)
            ,
            Weather(d['weather']['forecast6days'][0]['timeRelease'],
                    d['weather']['forecast6days'][0]['sky']['pmCode3day'],
                    d['weather']['forecast6days'][0]['sky']['pmName3day'],
                    None,
                    None,
                    d['weather']['forecast6days'][0]['temperature']['tmin3day'],
                    d['weather']['forecast6days'][0]['temperature']['tmax3day'],
                    None,
                    None,
                    None)
            ,
            Weather(d['weather']['forecast6days'][0]['timeRelease'],
                    d['weather']['forecast6days'][0]['sky']['pmCode4day'],
                    d['weather']['forecast6days'][0]['sky']['pmName4day'],
                    None,
                    None,
                    d['weather']['forecast6days'][0]['temperature']['tmin4day'],
                    d['weather']['forecast6days'][0]['temperature']['tmax4day'],
                    None,
                    None,
                    None)
        ]
