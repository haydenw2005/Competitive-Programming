#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3

num_cases = int(input())
    
for _ in range(num_cases):
    price, num_ppl  = [int(i) for i in input().split()]
    max_cents = [int(i) for i in input().split()]
    
    # if not enought money to pay, then it is impossible
    if sum(max_cents) < price:
            print("IMPOSSIBLE")
            continue
    
    divided_price = price//num_ppl
    
    contributions = []
    for max_cont in max_cents:
        #if not enough money to pay, then pay what you can
        if max_cont < divided_price:
            contributions.append(max_cont)
        else:
            contributions.append(divided_price)
            
    # now, we need to look at how much money is left over so we can redistribute
    debt = price - sum(contributions)
    debt_dist = debt//num_ppl
    
    # start keeping track of the money that could not be evenly distributed
    debt_remainder = debt%num_ppl
    
    #continue the follow logic until algo done:
    while True:
        # lets loop through each person, and have them pay as much debt as they can
        for i in range(num_ppl):
            #they can pay their full share of debt
            if (max_cents[i] >= contributions[i] + debt_dist):
                contributions[i] += debt_dist
                
            #they cant pay full share, so they pay what they can. 
            #people who have already paid as much as they can, will pay nothing (max_cents[i] - contributions[i] = 0)
            else:
                extra_debt = max_cents[i] - contributions[i]
                contributions[i] += extra_debt
                #add what ever they could not pay to the debt remainder
                debt_remainder += debt_dist - extra_debt
                
        #now, we only have debt_remainder left to distribute.
        #now lets distribute 1 cent to each person, by the size of their max constribution and if they can still pay more
        #note: this step could be optimized, but it works for now
        largest_remainder = sorted(range(num_ppl), key=lambda i: max_cents[i] - contributions[i], reverse=True)[:debt_remainder]
        for index in largest_remainder:
            if max_cents[index] > contributions[index]: 
                contributions[index] += 1
                debt_remainder -= 1
        
        #no debt remainder left to distribute, we are done
        if (debt_remainder == 0):
            break
        
        #else, we need to perform the debt distribution logic again, as we were not able to distribute the debt remainder
        debt_dist = debt_remainder//len(largest_remainder)
        debt_remainder = debt_remainder%num_ppl
    
    #print all the final contributions
    print(" ".join(map(str, contributions)))


