#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

import sys

num_scan_lines = 0;
isFirstLine = True
while True:
    
    #read the first line of input for each image, then check to see if it is not != 0 (EOF)
    try:
        num_scan_lines = int(next(sys.stdin))
        if num_scan_lines <= 0 or not num_scan_lines:
            break
    except:
        break

    prev = None
    current = 0
    isError = False
    
    #we want one line of space between each image
    if not isFirstLine: print() 
    else: isFirstLine = False
    
    # go line by line and decode the image
    for _ in range(num_scan_lines):
        scan_line = next(sys.stdin)
        data = scan_line.split()
        pixel_type = data[0]
        current = 0

        # now print either # or ., switching between them every time
        for index, pixel_count in enumerate(data[1:]):
            pixel_count = int(pixel_count)
            if (index % 2 == 0):
                print(pixel_type * pixel_count, end='')
            else: 
                print(("." if pixel_type == "#" else "#") * pixel_count, end='')
            current += pixel_count
        print()
        
        # if total pixel count is greater than 1000, create an error
        if (prev and prev != current or current > 1000):
            isError = True
        prev = current
    if isError:
        print("Error decoding image")
    