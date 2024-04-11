# 누적합)

# (1)
import sys
input = sys.stdin.readline

n = int(input())
ma = list(map(int,input().split()))

ans = max(ma)
for i in range(1, n-1):
    tmp = min(ma[i-1], ma[i+1])
    if tmp == 0 :
        continue

    ans = max(ans, tmp + ma[i])

print(ans)
