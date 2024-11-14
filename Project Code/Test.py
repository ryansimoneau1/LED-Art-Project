def break_hex_to_tuple(hex_list):
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

# Your original list
MyList = [0x00000000, 0x0000FF00, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x0000FF00, 0x00000000, 0x00000000, 0x0000FF00, 0x0000FF00]

# Call the function
result = break_hex_to_tuple(MyList)
for i, pixel in enumerate(MyList):
    pixel = pixel / 2
print(result)