from PIL import Image
import math
import numpy as np
def asciiArt(im, lim = None, lum = ' .,-~:;=!*#$@'):
    '''Returns an Ascii Art made from a PIL image. You can set limits of size for the image and the character list used for the Ascii Art'''
    ascArt = ""
    if lim != None:
        if im.size[0] > lim or im.size[1] > lim:
            im.thumbnail((lim, lim))
    mapp = lambda a, b, c, d, e: d + float(a - b) / float(c - b) * (e - d)
    i = 0
    for c in list(im.convert("RGBA").getdata()):
        if i % im.size[0] == 0 and not i  == 0: ascArt = ascArt + "\n"
        if c[3] > 250: ascArt = ascArt + str(lum[math.ceil(mapp((c[0] + c[1] + c[2]) / 3, 0, 255, len(lum) - 1, 0))]) + str(lum[round(mapp((c[0] + c[1] + c[2]) / 3, 0, 255, len(lum) - 1, 0))])
        else: ascArt = ascArt + lum[0] * 2
        i = i + 1
    return ascArt
def asciiArtFn(fn, lim = None, lum = ' .,-~:;=!*#$@'):
    '''Returns an Ascii Art made from an image with a given filename. You can set limits of size for the image and the character list used for the Ascii Art'''
    im = Image.open(fn)
    im.load()
    return asciiArt(im, lim, lum)
def unasciify(ascn: str, lum: str, inv: bool = False):
    '''Returns a grayscale PIL image made from an ascii art.'''
    if not inv: lum = lum[::-1]
    asc = ascn.replace("\n", "")[1::2]
    return Image.fromarray(np.uint8(np.reshape(np.array(list((lum.find(i) if lum.find(i) > -1 else 0)/(len(lum) - 1) for i in asc)),(int(len(ascn.split("\n")) - 1), int(len(ascn.split("\n")[1]) / 2))) * 255), 'L')
