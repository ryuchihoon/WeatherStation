#!/usr/bin/env python

# convert ./weather_icons/*.png file so that they have
# white background color and save into ./weather_icons_mod/*.png


from PIL import Image
import glob
import os
import numpy
from scipy.misc import imsave


def binarize_array(numpy_array, threshold, dark_val=0):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = dark_val
    return numpy_array

def main(args):
    binarize = args.mode == 'binary'
    threshold = args.threshold
    gray = args.mode == 'gray'
    darkval = args.darkval

    for fname in glob.glob("./weather_icons/*.png"):
        with Image.open(fname) as im:
            with Image.new("RGBA",im.size,"white") as canvas:
                out = Image.alpha_composite(canvas, im)
                outname = "./weather_icons_mod/" + os.path.split(fname)[1] 
                print("writing ",outname)
                if binarize:
                    out = out.convert('L')  # convert image to monochrome
                    image = numpy.array(out)
                    image = binarize_array(image, threshold, darkval)
                    imsave(outname, image)
                elif gray:
                    out = out.convert('L')  # convert image to monochrome
                    out.save(outname)
                else :
                    out.save(outname)


def get_parser():
    """Get parser object for script"""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", "--mode",
                        dest="mode",
                        help="one of binary,gray,color",
                        default='binary',
                        type=str,
                        required=False)
    parser.add_argument("-t", "--threshold",
                        dest="threshold",
                        help="brightness threshold when mode is binary",
                        default=250,
                        type=int,
                        required=False)
    parser.add_argument("--darkval",
                        dest="darkval",
                        help="target dark bright when mode is binary",
                        default=90,
                        type=int,
                        required=False)
    return parser

if __name__=='__main__':
    args = get_parser().parse_args()
    print("args:", args)
    main(args)