import utime
import machine
from neopixel import Neopixel
from LEDdata import IDLE_frames, DRAIN_frames, water_colors
import os
import sys

# LED Strip and Matrix sizes
numpix_strip  = 50 + len(water_colors)
numpix_screen = 256

# Size water_colors list to acccount for drain effect
for i in range(numpix_strip-len(water_colors)):
    water_colors.append(0)
#-------------------------------------------#
#											
#											
#				FUNCTIONS					
#											
#											
#-------------------------------------------#
# Break LEDMatrixStudio outputs into Tuples for Neopixel Library
def hex_to_tuple(hex_list):
    result = []
    for hex_value in hex_list:
        
        # Break into 3 parts
        upper = (hex_value >> 16) & 0xFF
        middle = (hex_value >> 8) & 0xFF
        lower = hex_value & 0xFF
        
        # Append the tuple to the result list
        result.append((upper, middle, lower))
    
    return result

def render_frame(frames, LED_Matrix, frame_num):
    output_frame = frames[frame_num]
    output_frame = hex_to_tuple(output_frame)
    
    for i, pixel in enumerate(output_frame):
            LED_Matrix.set_pixel(i, pixel)
            
# Shift LED strip colors onto the LED strip
def water_drain(LEDList, WaterList, frame):
    frm = frame - 1
    for i in range(frm):
        LEDList.set_pixel(i,WaterList[frm])
        frm -= 1
        
# Convert ADC Values to Voltages
def adc_to_volts(adc_val):
    volts = (3.3/65536)*adc_val # u Python converts 12 bit ADC to 16 bit via left shift
    return volts

#-------------------------------------------#
#											
#											
#					LEDs					
#											
#											
#-------------------------------------------#
# Define LED strip and Matrix structures
strip 	= Neopixel(numpix_strip, 1, 13, "RGB") # 10 on breadboard, 13 on perf
screen 	= Neopixel(numpix_screen, 2,15, "GRB")

# Set LED Brightness
strip.brightness(255)
screen.brightness(45)

# Convert water color effects into Tuples
water_colors = hex_to_tuple(water_colors)

#-------------------------------------------#
#											
#											
#				LIGHT SENSOR				
#											
#											
#-------------------------------------------#

Light_sensor = machine.ADC(0)

#-------------------------------------------#
#											
#											
#				MAIN LOOP					
#											
#											
#-------------------------------------------#
control_state = "IDLE"
num_led_drain = numpix_strip

# Frame Count Variables
strip_count = 0
screen_count = 0

waterfall_start_flag = 0
drain_complete_flag = 0

screen_done_flag = 0
waterfall_delay = 3 # water begins to drop at frame 2
drain_end_delay = 4

while True:
    # Clock to control the frame rate of the displays
    utime.sleep(0.1)
    Ballot = Light_sensor.read_u16()
    Ballot = adc_to_volts(Ballot)
    
    # Determine state
    if control_state == "IDLE":
        if Ballot > 2:
            control_state = "DRAIN"
            strip_count = 0
            screen_count = 0
        else:
            # render the Idle screen animation continuously
            render_frame(IDLE_frames, screen, screen_count)
            screen.show()
            screen_count += 1
            
            if screen_count >= len(IDLE_frames):
                screen_count = 0
    
    elif control_state == "DRAIN":
        if screen_done_flag == 0:
            render_frame(DRAIN_frames, screen, screen_count)
            screen.show()
            
            if screen_count == waterfall_delay:
                waterfall_start_flag = 1 # Start the waterfall after a certain number of screen frames
            
            screen_count += 1
            
            
            if screen_count >= len(DRAIN_frames):
                screen_count = 0
                screen_done_flag = 1
        
        if waterfall_start_flag == 1:
            water_drain(strip, water_colors, strip_count)
            strip.show()
            strip_count += 1
            
            if strip_count >= numpix_strip:
                strip_count = 0
                drain_complete_flag = 1
            
        if (Ballot < 2) and (drain_complete_flag == 1) and (strip_count == 0):
            utime.sleep(drain_end_delay) # wait a moment to go back to the idle state. for the feel of the project
            control_state = "IDLE"
            strip_count = 0
            screen_count = 0
            screen_done_flag = 0
            drain_complete_flag = 0
            waterfall_start_flag = 0

# # Get file system statistics
# stat = os.statvfs('/')
# 
# # Compute total and free flash memory
# block_size = stat[0]
# total_blocks = stat[2]
# free_blocks = stat[3]
# 
# total_flash_memory = block_size * total_blocks
# free_flash_memory = block_size * free_blocks
# 
# # Print results in MB
# print(f"Total flash memory: {total_flash_memory / (1024 ** 2):.2f} MB")
# print(f"Free flash memory: {free_flash_memory / (1024 ** 2):.2f} MB")




