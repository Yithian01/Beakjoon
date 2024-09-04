# 정렬후 LIS를 구해 최대 n - LIS를 빼준다.

# 시간 복잡도 계산: O(N^2)
import sys
input = sys.stdin.readline

n = int(input())
ma = []
dp = [1] * (n+1)

for _ in range(n):
    a, b=  map(int, input().split())
    ma.append((a,b))

ma.sort()

for i in range(1, n):
    for j in range(0, i):
        if ma[j][1] < ma[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(n - max(dp))
