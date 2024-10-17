#Author: Hayden White


alphabet_len = 26
dp = [0] * alphabet_len  # DP array for storing the length of subsequence ending at each letter

string = input()

for ch in string:
    alphabet_index = ord(ch) - ord('a')
    
    # Find the maximum subsequence length ending at any previous character
    max_prev = 0
    for i in range(alphabet_index):
        max_prev = max(max_prev, dp[i])
    
    # Update the dp value for the current character
    dp[alphabet_index] = max(dp[alphabet_index], max_prev + 1)

# Find the longest subsequence length and print the number of missing characters
print(alphabet_len - max(dp))