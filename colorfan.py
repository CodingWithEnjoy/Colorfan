red = [205, 0, 0]
green = [0, 205, 0]
white = [255, 255, 255]
black = [0, 0, 0]
gray = [50, 50, 50]
blue = [0, 0, 205]
yellow = [255, 230, 0]
magenra = [255, 0, 255]
cyan = [0, 255, 255]
olive = [128, 128, 0]
navy = [0, 0, 128]
lime = [0, 255, 0]
aqua = [0, 255, 255]
violet = [238, 130, 238]
deep_pink = [255, 20, 147]
saddle_brown = [244, 164, 96]

def _gncolor(color,c):
        colorcode = ""
        if color != False:
            vl = 0
            if type(color) == int:
                vl = color
                color = [color]
            while len(color) < 3:
                color.append(vl)
            r = color[0]
            g = color[1]
            b = color[2]
            colorcode += "\033["+c+";2;{};{};{}m".format(r, g, b)
        return colorcode

def colorize(fgcolor=False, bgcolor=False, weight=0):
    return _gncolor(fgcolor,"38") + _gncolor(bgcolor,"48")+"\033["+str(weight)+"m"

def fgcolor(fgcolor):
    return _gncolor(fgcolor,"38")

def bgcolor(bgcolor):
    return _gncolor(bgcolor,"48")

def uncolor():
    return "\033[0m"
