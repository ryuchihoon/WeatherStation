class WeatherSource(object):
    def __init__(self, params):
        self.params = params
    
    def get_curr_weather(self):
        raise NotImplementedError()
    
    def get_weather_forecast(self):
        raise NotImplementedError()