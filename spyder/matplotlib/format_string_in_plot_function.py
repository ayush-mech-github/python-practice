# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:31:52 2020

@author: AAYUSH pc
"""


#fmt=[color][marker][line] or fmt=[marker][line][color]
#by default, it takes color from color cycle
#b-   blue,solid line
#o-   orange,solid line
#g-   green,solid line

import matplotlib.pyplot as plt

#fmt=[color][marker][line]
plt.plot([10,20,30,40],[2,4,6,8],"ro-")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#supported color abbreviations
#character        color
#'b'               blue
#'g'               green
#'r'               red
#'c'               cyan
#'m'               magenta
#'y'               yellow
#'k'               black
#'w'               white


#markers abbreviations
# "."		point
# ","		pixel
# "o"		circle
# "v"		triangle_down
# "^"		triangle_up
# "<"		triangle_left
# ">"		triangle_right
# "1"		tri_down
# "2"		tri_up
# "3"		tri_left
# "4"		tri_right
# "8"		octagon
# "s"		square
# "p"		pentagon
# "P"		plus (filled)
# "*"		star
# "h"		hexagon1
# "H"		hexagon2
# "+"		plus
# "x"		x
# "X"		x (filled)
# "D"		diamond
# "d"		thin_diamond
# "|"		vline
# "_"		hline

#linestyles
#character     description
#"-"           solid line style
#"--"          dashed line style
#"-."          dash-dot line style
#":"           dotted line style

import numpy as np

arr=np.arange(0,10,2)
plt.plot(arr,"go-",arr**3,"rD--",arr**2,"b*:")