import sys
input= sys.stdin.readline
INF = 10**9 + 7 

ans = 0
s = input().rstrip()
for idx, val in enumerate(s):
    if val == 'O':
        ans += (2 ** idx) 
        ans %= INF


print(ans)