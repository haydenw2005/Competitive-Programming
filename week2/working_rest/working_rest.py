#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

import sys

stack_one = []
stack_two = []

while True:
    n = int(input())
    if (n == 0): break
    
    for i in range(n):
        instruction, m = input().split()
        m = int(m)
        
        #drop
        if instruction == "DROP":
            stack_one.extend([None] * m)
            print("DROP 1", m)
            
        #take
        elif instruction == "TAKE":
            
            #move
            if (len(stack_two) < m):
                diff = m - len(stack_two)
                print("MOVE 1->2", diff)
                stack_two.extend([None] * diff)
                stack_one = stack_one[:diff]
                
            stack_two = stack_two[:len(stack_two) - m]
            print("TAKE 2", m)
    print()