#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

import sys
import io

# https://www.geeksforgeeks.org/byte-objects-vs-string-python/
# for this submission, I am trying to use byte objects instead of strings
# might fix my TLE issues

def join_strings():
    input = io.BytesIO(sys.stdin.buffer.read()).readline
    num_strings = int(input())

    strings = []

    for _ in range(num_strings):
        strings.append(input().rstrip(b'\n'))
    
    if len(strings) == 1:
        print(strings[0].decode())
        return
    
    for j in range(num_strings - 1):
        firstIndex, secondIndex = map(int, input().rstrip(b'\n').split())
        strings[firstIndex - 1] = b''.join([strings[firstIndex - 1], strings[secondIndex - 1]])
        strings[secondIndex - 1] = b''
        
    for s in strings:
        if s:
            print(s.decode())
            return

    print("")

join_strings()