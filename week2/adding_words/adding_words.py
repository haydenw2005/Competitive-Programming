#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

import sys

#bi-directional mapping so we can see what values correspond to defintions and vice verse
# both need to be unqiue so we have to use bidirectional, values and defs must be keys
defintion_to_val = {}
val_to_def = {}

for command in sys.stdin:

    #update both mappings with new definitions
    if command.startswith("def"):
        word = command.split()[1]
        value = int(command.split()[2])
        
        #Make sure to remove old value from val_to_def
        if word in defintion_to_val:
            old_value = defintion_to_val[word]
            del val_to_def[old_value]
            
        defintion_to_val[word] = value
        val_to_def[value] = word
        
    #clear both mappings
    elif command.startswith("clear"):
        defintion_to_val.clear()
        val_to_def.clear()
        
    elif command.startswith("calc"):
        unknown = False
        expression = command.split()[1:]
        
        result = 0
        current_op = '+'
        
        #calculate new val
        for token in expression:
            if (token == "=" or token is None):
                break
            if (token == "+" or token == "-"):
                current_op = token
            else:
                def_val = defintion_to_val.get(token, None)
                if def_val is None:
                    unknown = True
                    break
                # perform the operation
                if current_op == "+": result += def_val
                else: result -= def_val
            
        # check if we have the result saved
        # print result of expression       
        new_val = val_to_def.get(result, None)
        if new_val is None or unknown is True:
            print(" ".join(expression) + " unknown")
        else:
            print(" ".join(expression) + " " + new_val)

                
                
                
    