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
    if not args['fontpath']:
        args['fontpath'] = os.environ.get('WEATHER_STATION_FONT_PATH')

    print("Arguments : %s"%args)

    weather_src = SKPWeather(args)

    cur_weather = weather_src.get_curr_weather()
    print("Cur weather : %s"%str(cur_weather))
    print("Cur airqual : %s"%cur_weather.air_quality)
    weather_forecast = weather_src.get_weather_forecast()
    print("Weather forecast : %s"%weather_forecast)

    renderer = PapirusRenderer(args['rotate'], font_path=args['fontpath'])
    renderer.render(cur_weather, weather_forecast)


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
    parser.add_argument('--fontpath',
                        help='Path to font file. ttf or otf',
                        default=None)
    return parser

if __name__ == '__main__':
    main(vars(get_parser().parse_args()))
