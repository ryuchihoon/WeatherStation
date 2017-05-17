class WeatherSource:
    def __init__(self, params):
        self.params = params
    
    def get_curr_weather(self):
        raise NotImplementedError()
    
    def get_curr_air(self):
        raise NotImplementedError()
    
    def get_weather_forecast(self):
        raise NotImplementedError()