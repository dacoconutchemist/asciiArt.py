from PIL import Image
import math
def asciiArt(im, lim = None, lum = ' .,-~:;=!*#$@'):
    '''Return an Ascii Art made from a PIL image. You can set limits of size for the image and the character list used for the Ascii Art'''
    ascArt = ""
    if lim != None:
        if im.size[0] > lim or im.size[1] > lim:
            im.thumbnail((lim, lim))
    mapp = lambda a, b, c, d, e: d + float(a - b) / float(c - b) * (e - d)
    i = 0
    for c in list(im.getdata()):
        if i % im.size[0] == 0: ascArt = ascArt + "\n"
        ascArt = ascArt + str(lum[math.ceil(mapp((c[0] + c[1] + c[2]) / 3, 0, 255, len(lum) - 1, 0))]) + str(lum[round(mapp((c[0] + c[1] + c[2]) / 3, 0, 255, len(lum) - 1, 0))])
        i = i + 1
    return ascArt
def asciiArtFn(fn, lim = None, lum = ' .,-~:;=!*#$@'):
    '''Return an Ascii Art made from an image with a given filename. You can set limits of size for the image and the character list used for the Ascii Art'''
    im = Image.open(fn)
    im.load()
    return asciiArt(im, lim, lum)
