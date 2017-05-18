from collections import namedtuple

Weather = namedtuple('Weather', 'time,weather_code,weather_desc,weather_icon,' + \
                                'cur_temperature,min_temperature,max_temperature,' + \
                                'humidity,air_quality,air_quality_icon')