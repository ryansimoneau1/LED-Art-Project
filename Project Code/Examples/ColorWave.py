# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import time
from neopixel import Neopixel

numpix_strip = 50
numpix_screen = 256
strip 	= Neopixel(numpix_strip, 1, 10, "GRB")
screen 	= Neopixel(numpix_screen, 2,13, "GRB")
# strip = Neopixel(numpix, 0, 0, "GRBW")

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

# same colors as normaln rgb, just 0 added at the end
# colors_rgbw = [color+tuple([0]) for color in colors_rgb]
# colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
colors = colors_rgb
# colors = colors_rgbw


step_strip = round(numpix_strip / len(colors))
current_pixel_strip = 0
step_screen = round(numpix_screen / len(colors))
current_pixel_screen = 0

strip.brightness(50)
screen.brightness(10)

for color1, color2 in zip(colors, colors[1:]):
    strip.set_pixel_line_gradient(current_pixel_strip, current_pixel_strip + step_strip, color1, color2)
    screen.set_pixel_line_gradient(current_pixel_screen, current_pixel_screen + step_screen, color1, color2)
    current_pixel_strip += step_strip
    current_pixel_screen += step_screen

strip.set_pixel_line_gradient(current_pixel_strip, numpix_strip - 1, violet, red)
screen.set_pixel_line_gradient(current_pixel_screen, numpix_screen - 1, violet, red)

while True:
    strip.rotate_right(1)
    screen.rotate_right(1)
    time.sleep(0.0042)
    strip.show()
    screen.show()


