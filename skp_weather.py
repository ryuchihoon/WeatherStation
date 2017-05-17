from weather_source import WeatherSource


class SKPWeather(WeatherSource):
    def __init__(self, params):
        super().__init__(params)
        self.appkey = params['appkey']
        self.lat = params['lat']
        self.lon = params['lon']
    
    def get_curr_weather(self):
        return "OK"
    
    def get_curr_air(self):
        return "GOOD"
    
    def get_weather_forecast(self):
        return "BAD"
