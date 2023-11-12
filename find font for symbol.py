from fontTools.ttLib import TTFont
import matplotlib.font_manager as mfm

def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False

# uni_char =  u"✹"
uni_char = u"\u2208"

font_info = [(f.fname, f.name) for f in mfm.fontManager.ttflist]

for i, font in enumerate(font_info):
    if char_in_font(uni_char, TTFont(font[0])):
        print(font[0], font[1])