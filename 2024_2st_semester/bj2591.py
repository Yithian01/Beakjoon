import sys
input = sys.stdin.readline
'''

    2 7 1 2 3 
    1 1

'''
s = input().rstrip()
dp = [0] * (len(s) + 1)
dp[0] = 1
dp[1] = 1


for i in range(2, len(s)+1):

    if int(s[i-1]) != 0:
        dp[i] = dp[i-1]
    
    if int(s[i-2]) != 0 and int(s[i-2] + s[i-1]) <= 34:
        dp[i] += dp[i-2]


print(dp[len(s)])