# author: @hayden-white
# consent to share

#! /usr/bin/python3
import sys

num_lines = int(next(sys.stdin))
for instruction in sys.stdin:
    if instruction.startswith("Simon says"):
        #nice and easy string split after "Simon says"
        print(instruction.split("Simon says")[1].rstrip('\n'))