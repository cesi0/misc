#!/usr/bin/python

from time import sleep
import sys

h = "      _____           _____"
a = """I8                             8I
 Yb,      HAPPY   V-DAY      ,dP"""
k = '             "8b d8"   '
b = """dP'           "8a8"           `Yd
8(              "              )8"""
i = "          `88,     ,88'"
t = ' d8P"      "Y8b, ,d8P"      "Y8b"'
c = '            "8b   d8"  '
H = '      "Yba             adP"'
s = """              `888'
                 "
"""
g = '  "8a,                     ,a8"'
o = "  ,ad8PPPP88b,     ,d88PPPP8ba,"
O = '    "8a,                 ,a8"'
d = "        `Y8a         a8P'"


vd = '{} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}'.format(h,o,t,b,a,g,O,H,d,i,c,k,s)

def slowtext(text):
	for c in text:
		print c,
		sys.stdout.flush()
		sleep(0.02)

slowtext(vd)
