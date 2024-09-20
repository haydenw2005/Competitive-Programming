#Author: Hayden White
#It is ok to share my code anonymously for educational purposes
#! /usr/bin/python3


n, k = [int(i) for i in input().split()]


arr = [int(i) for i in input().split()]

min_answer = max(arr)

max_answer = sum(arr)


def calculate_min_box(ans):
    current_max = float(0)
    total_partitions = 0
    current_partition = 0
    
    for item in arr:
        if (current_partition + item <= ans):
            current_partition += item
        else:
            if current_partition > current_max:
                current_max = current_partition
            
            current_partition = 0   
            total_partitions += 1
    
    print(total_partitions, current_max)
    return (total_partitions, current_max)


while (min_answer < max_answer):
    # print(min_answer, max_answer)
    mid_ans = (min_answer + max_answer) // 2
    
    total_partitions, current_max = calculate_min_box(mid_ans)
    
    print(total_partitions, current_max, mid_ans)
    if (total_partitions == k):
        print(current_max)
        break
    
    if (total_partitions < k):
        max_answer = mid_ans
    else:
        min_answer = mid_ans
    
    
    
    

        

