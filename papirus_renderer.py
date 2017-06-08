#-- coding: utf-8 --

import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

import collections
from PIL import Image, ImageOps, ImageDraw, ImageFont


code_2_icono = collections.defaultdict(lambda : '38')
kor_2_eng = collections.defaultdict(lambda : 'UNKNOWN')

code_2_icono['SKY_O00'] = ['38']
code_2_icono['SKY_O01'] = ['01', '08']
code_2_icono['SKY_O02'] = ['02', '09']
code_2_icono['SKY_O03'] = ['03', '10']
code_2_icono['SKY_O04'] = ['12', '40']
code_2_icono['SKY_O05'] = ['13', '41']
code_2_icono['SKY_O06'] = ['14', '42']
code_2_icono['SKY_O07'] = ['18']
code_2_icono['SKY_O08'] = ['21']
code_2_icono['SKY_O09'] = ['32']
code_2_icono['SKY_O10'] = ['04']
code_2_icono['SKY_O11'] = ['29']
code_2_icono['SKY_O12'] = ['26']
code_2_icono['SKY_O13'] = ['27']
code_2_icono['SKY_O14'] = ['28']

code_2_icono['SKY_W00'] = ['38']
code_2_icono['SKY_W01'] = ['01', '08']
code_2_icono['SKY_W02'] = ['02', '09']
code_2_icono['SKY_W03'] = ['03', '10']
code_2_icono['SKY_W04'] = ['18']
code_2_icono['SKY_W07'] = ['21']
code_2_icono['SKY_W09'] = ['12', '40']
code_2_icono['SKY_W10'] = ['21']
code_2_icono['SKY_W11'] = ['04']
code_2_icono['SKY_W12'] = ['13', '41']
code_2_icono['SKY_W13'] = ['32']


kor_2_eng[u'좋음'] = ['GOOD']
kor_2_eng[u'보통'] = ['NORMAL']
kor_2_eng[u'나쁨'] = ['BAD']
kor_2_eng[u'매우 나쁨'] = ['V BAD']


def geticonfname(code):
    l = code_2_icono[code]
    dname = os.path.join(os.path.dirname(__file__), "resources", "weather_icons_mod")
    if len(l) > 1:
        return os.path.join(dname, l[0] + '.png')
    else:
        return os.path.join(dname, l[0] + '.png')


BLACK = 0
WHITE = 1



class PapirusRenderer:
    """Renderer for Papirus HAT"""

    def __init__(self, rotate=0, font_path=None):
        if font_path:
            self.font_path = font_path
        else:
            self.font_path = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

        print("rotate:",rotate)

        try:
            from papirus import Papirus
            self.papirus = Papirus(rotate=rotate)
            self.canvas_size = self.papirus.size
        except ImportError:
            print("papirus import failed")
            self.papirus = None
            self.canvas_size = (272,192)

    
    def render(self, weather, weather_forecast):
        
        canvas = Image.new('1', self.canvas_size, WHITE)

        print("font_path:",self.font_path)

        fname = geticonfname(weather.weather_code)
        print("file:",fname)
        self._drawImage(canvas, fname, 20,5,(100,100))
        print("cur desc : %s"%str(weather.weather_desc))
        print("cur airq : %s"%str(weather.air_quality))
        temperature = str(weather.cur_temperature).split('.')[0] + u" \u2103"
        self._drawText(canvas, temperature, 70,120, font_size=20, center_horizontal=True)
        translated = kor_2_eng[weather.air_quality][0]
        print("cur airq translated: %s"%translated)
        self._drawText(canvas, translated, 70,140, font_size=20, center_horizontal=True)
        
        base_x,base_y = 145,10
        for i,w in enumerate(weather_forecast):
            fname = geticonfname(w.weather_code)
            self._drawImage(canvas, fname, base_x, base_y+55*i, (50,50))
            temperature = str(w.min_temperature) + " / " + str(w.max_temperature)
            self._drawText(canvas, temperature, base_x+80, base_y+28+55*i, font_size=14, center_horizontal=True)

        if self.papirus == None:
            # save a image for debugging purpose
            with open("result.jpg", "wb") as fp:
                canvas.save(fp)
                print("result file saved")
        else:
            self.papirus.display(canvas)
            self.papirus.update()


    def _drawImage(self, canvas, image_path, x, y, size):
        image = Image.open(image_path)
        image = ImageOps.grayscale(image)
        image = image.resize(size)
        image = image.convert("1", dither=Image.FLOYDSTEINBERG)
        canvas.paste(image,(x,y))


    def _drawText(self, canvas, text, x, y, font_size=20, center_horizontal=False):
        draw = ImageDraw.Draw(canvas)
        font = ImageFont.truetype(self.font_path, font_size)
        text_draw_size = draw.textsize(text, font=font)
        if center_horizontal:
            x = x - text_draw_size[0]/2
        draw.text( (x, y) , text, font=font, fill=BLACK)
