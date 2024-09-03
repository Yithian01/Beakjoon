# %연산을 통해서 해당 index가 어디에 해당 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = list(map(int, input().split()))
q = list(map(int, input().split()))

# A의 범위가 극도로 낮다 21 정도 
num = [[] for _ in range(n)]

dp = []
# n-1 ~~ 0, 1, 2
for i in range(n):
    tmp = 1
    for j in range(4):
        cnt = (i + j ) % n
        num[cnt].append(i)
        
        tmp *= ma[cnt]
            
    dp.append(tmp)

ans = sum(dp)
for i in q:
    for j in num[i-1]:
        ans += dp[j] * -2
        dp[j] *= -1
    
    print(ans)