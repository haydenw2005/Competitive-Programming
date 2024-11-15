# Author: Hayden White

while True:
    seq = [int(i) for i in input().split()]
    if len(seq) == 1 and seq[0] == 0:
        break

    n = seq[0]
    seq = seq[1:]
    
    # create and use an array to track the largest possible subsequence at each i
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # back track from the length of the largest subsequence to form the correct subsequence
    result_sequence = []

    # get the largest value from the dp array, which happens to be the length of the largest subsequence
    seq_len = max(dp)
    count = seq_len
    current_p = n - 1
    
    while (0 < seq_len and current_p > -1):
        # add the last occurence of the current count value to the subsequence array
        if (dp[current_p] == count):
            count -= 1
            result_sequence.append(seq[current_p])
        current_p -= 1
        
    # reverse and join the backtracked sequence
    result_sequence.reverse()
    print(seq_len, " ".join(map(str, result_sequence)))
    
