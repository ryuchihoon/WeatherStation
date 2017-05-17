#!/usr/bin/env python

import os
import argparse
from skp_weather import SKPWeather

def main(args):
    if not args['appkey']:
        args['appkey'] = os.environ.get('WEATHER_STATION_APP_KEY')
    if not args['lat']:
        args['lat'] = os.environ.get('WEATHER_STATION_LAT')
    if not args['lon']:
        args['lon'] = os.environ.get('WEATHER_STATION_LON')

    print("Arguments : %s"%args)

    weather_src = SKPWeather(args)

    cur_weather = weather_src.get_curr_weather()
    print("Cur weather : %s"%cur_weather)
    cur_air = weather_src.get_curr_air()
    print("Cur air : %s"%cur_air)
    weather_forecast = weather_src.get_weather_forecast()
    print("Weather forecast : %s"%weather_forecast)


if __name__ == '__main__':
    os.environ.get('ws_appkey')
    parser = argparse.ArgumentParser()
    parser.add_argument('--appkey', help='SK Planet App Key')
    parser.add_argument('--lat', help='Lattitude of the location')
    parser.add_argument('--lon', help='Longitude of the location')
    main(vars(parser.parse_args()))
