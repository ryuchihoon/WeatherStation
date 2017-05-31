#!/usr/bin/env python

import os
import argparse
from skp_weather import SKPWeather
from papirus_renderer import PapirusRenderer

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
    print("Cur weather : %s"%str(cur_weather))
    weather_forecast = weather_src.get_weather_forecast()
    print("Weather forecast : %s"%weather_forecast)

    renderer = PapirusRenderer(args['rotate'])
    renderer.render(cur_weather)


def get_parser():
    """Get parser object for script"""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--appkey', help='SK Planet App Key')
    parser.add_argument('--lat', help='Lattitude of the location')
    parser.add_argument('--lon', help='Longitude of the location')
    parser.add_argument('--rotate',
                        help='Rotation of epaper display',
                        default=0,
                        type=int)
    return parser

if __name__ == '__main__':
    main(vars(get_parser().parse_args()))
