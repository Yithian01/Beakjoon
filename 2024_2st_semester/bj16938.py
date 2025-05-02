import sys
input = sys.stdin.readline
INF = sys.maxsize
'''

    L <= x <= R
    max - min >= x 


'''

n, L, R, X = map(int, input().split())
ma = list(map(int, input().split()))

ans = 0
for bit in range(1 << n):
    
    cnt = 0
    add, res = 0, [INF, 0]
    for i in range(n):
        if 1 << i & bit:
            cnt += 1
            add += ma[i]
            res[0] = min(res[0], ma[i])
            res[1] = max(res[1], ma[i])

    if cnt < 2 or L > add or R < add or res[1] - res[0] < X:

        continue

    ans += 1

print(ans)

    
            
