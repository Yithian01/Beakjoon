# 26 * n => 최대 
import sys
input = sys.stdin.readline
ma = {}

for i in range(26):
    tmp = 65 + i
    tmp = chr(tmp)
    ma[i+1] = tmp



n, m = map(int, input().split())
if 26 * n < m or m - n < 0 : 
    print('!')
    exit(0)


dp = [1] * n
ans = m - n

for i in range(n):
    if ans <= 0:
        break
    ans += 1
    tmp = 1
    while tmp < 26:
        tmp += 1
        if ans - tmp <= 0:
            break
    
    ans -= tmp
    dp[i] = tmp


for i in range(n-1, -1, -1):  
    print(ma[dp[i]],end='')