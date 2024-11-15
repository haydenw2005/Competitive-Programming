#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

import sys

word = next(sys.stdin)

#cuz no word should be lexigraphically greater than this
smallestWord = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

for i in range(1, len(word) - 2):

    # j should never be less than i
    for j in range(i + 1, len(word) - 1):
        #split in to also possible sub sections
        first_partition = word[:i].strip()
        second_partition = word[i:j].strip()
        third_partition = word[j:].strip()

        #now reverse them
        new_word = first_partition[::-1] + second_partition[::-1] + third_partition[::-1]

        #check to see if smallest, if it is, then update smallestWord
        if new_word < smallestWord:
            smallestWord = new_word

print(smallestWord)
