import collections
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

code_2_icono = collections.defaultdict(default='38')

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

def geticonfname(code):
    l = code_2_icono[code]
    if len(l) > 1:
        return "./resources/weather_icons_mod/" + l[0] + '.png'
    else:
        return "./resources/weather_icons_mod/" + l[0] + '.png'


class PapirusRenderer:
    """Renderer for Papirus HAT"""

    def __init__(self, rotate=0):
        self.rotate = rotate

        try:
            from papirus import PapirusComposite
            self.pcomp = PapirusComposite(False)
            self.pcomp.AddImg(geticonfname('SKY_W00'), 20, 20, (80,80), Id="mainIcon")
            self.pcomp.AddText('Unknown', 0, 120, Id="mainText")
            self.pcomp.WriteAll()
        except ImportError:
            self.pcomp = None

    
    def render(self, weather):
        if self.pcomp == None:
            pass
        
        fname = geticonfname(weather.weather_code)
        print("file:",fname)
        self.pcomp.UpdateImg("mainIcon", fname)
        self.pcomp.UpdateText("mainText", str(weather.weather_desc))
        self.pcomp.WriteAll()
