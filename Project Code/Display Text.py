# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import time
from neopixel import Neopixel

# VoteOr = [
# 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 
# 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 
# 0x0000FF00, 0x000000FF, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x000000FF, 0x000000FF, 0x000000FF, 0x0000FF00, 0x000000FF, 0x000000FF, 0x000000FF, 0x0000FF00, 0x000000FF, 0x000000FF, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x000000FF, 0x000000FF, 0x000000FF, 0x0000FF00, 0x000000FF, 0x000000FF, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 
# 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 
# 0x0000FF00, 0x000000FF, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x000000FF, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x000000FF, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 
# 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 
# 0x0000FF00, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x000000FF, 0x000000FF, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x000000FF, 0x000000FF, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x000000FF, 0x000000FF, 0x000000FF, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x000000FF, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 0x0000FF00, 
# 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 
# ]

WOW = [
0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x00FF0000, 0x000080FF, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x00FF0000, 0x000080FF, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x00FF0000, 0x000080FF, 0x00FF0000, 0x00FF0000, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x00FF0000, 0x00FF0000, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x00FF0000, 0x00FF0000, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x00FF0000, 0x00FF0000, 0x00FF0000, 0x000000FF, 
0x00FFFFFF, 0x00FF0000, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000080FF, 0x000000FF, 
0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 0x00FFFFFF, 0x000000FF, 

]
def hex_to_tuple(hex_list):
    result = []
    for hex_value in hex_list:
        # Extract the bottom 6 hex digits
        bottom_6 = hex_value & 0xFFFFFF
        
        # Break into 3 parts
        upper = (bottom_6 >> 16) & 0xFF
        middle = (bottom_6 >> 8) & 0xFF
        lower = bottom_6 & 0xFF
        
        # Append the tuple to the result list
        result.append((upper, middle, lower))
    
    return result

numpix_strip = 50
numpix_screen = 256
strip 	= Neopixel(numpix_strip, 1, 10, "GRB")
screen 	= Neopixel(numpix_screen, 2,13, "GRB")
# strip = Neopixel(numpix, 0, 0, "GRBW")

red 	= (255, 0, 0)
orange 	= (255, 50, 0)
yellow 	= (255, 100, 0)
green 	= (0, 255, 0)
blue 	= (0, 0, 255)
indigo 	= (100, 0, 90)
violet 	= (200, 0, 100)

blue 	= (0,0,255)
teal			= (0,128,128)
turquoise		= (72,209,204)
purple			= (128,0,128)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

# water_colors = [midnight_blue, teal, aqua, persian_indigo, black]
water_colors = [teal, blue, teal]
# same colors as normaln rgb, just 0 added at the end
# colors_rgbw = [color+tuple([0]) for color in colors_rgb]
# colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
colors = colors_rgb
water = water_colors
# colors = colors_rgbw


step_strip = round(numpix_strip / len(water))
current_pixel_strip = 0

strip.brightness(50)
screen.brightness(10)

for color1, color2 in zip(water, water[1:]):
    strip.set_pixel_line_gradient(current_pixel_strip, current_pixel_strip + 3, color1, color2)
    current_pixel_strip += 3
    

LEDFrame = hex_to_tuple(WOW)
NewList = []
for i, pixel in enumerate(LEDFrame):
    screen.set_pixel(i, pixel)
    NewList.append(pixel)
    
    
print(NewList)    
# strip.set_pixel_line_gradient(current_pixel_strip, numpix_strip - 1, aqua, teal)
# screen.set_pixel_line_gradient(current_pixel_screen, numpix_screen - 1, violet, red)

flag = 0

while True:
    
    time.sleep(0.005)
    flag += 1
#     screen.rotate_right(1)
    screen.show()
    if flag == 20:
        strip.rotate_right(1)
        strip.show()
        flag = 0




