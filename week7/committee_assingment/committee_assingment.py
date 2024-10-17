#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3



while True:

    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    committees = [set()]
    
    for _ in range(m):
        pair = input().split()
        
        committee_found = False
        for committee in committees:
            if  pair[0] not in committee and pair[1] not in committee:
                committee.add(pair[0])
                committee.add(pair[1])
                committee_found = True
                break
        
        if not committee_found:
            committees.append(set(pair))
            
    print(len(committees))
    #print(committees)
            
            
