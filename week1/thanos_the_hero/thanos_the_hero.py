#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

import sys


def kill_people():
    # get the number of planets and the populations of each planet
    num_planets = int(next(sys.stdin))
    populations = list(map(int, next(sys.stdin).split()))

    prev = populations[num_planets - 1]
    total_kills = 0

    # loop backward through the planets so we can easily check if a planet population
    # needs to be reduced
    for i in range(2, num_planets + 1):
        population = populations[num_planets - i]

        # thanos kills himself, prune condition if index is greater than population
        # we know that there is no chance the populations will make thanos happy
        if (i > population):
            print("1")
            return
        
        # main logic to kill the people if population needs to be reduced and add
        # to the count ofhow many people thanos killed
        if (population > prev):
            total_kills += (population - prev) + 1
            prev = population - ((population - prev) + 1)
        # must be stricly bigger, so if equal then thanos kills himself
        elif (prev == population):
            print("1")
            return
        else:
            prev = population
            
    print(total_kills)

kill_people()

    
