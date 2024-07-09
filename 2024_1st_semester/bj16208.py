from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 1e9


# n개의 막대가 필요 
# but 1개의 막대를 가지고 있음
# x + y 막대 자를 때 xy의 곱ㅇ ㅣ필요 
# 최소 비용으로 n개 막대 필요 <--------- 이분탐색

# 비용이 커질수록 n은 
n = int(input())
ma = list(map(int, input().split()))
q =  [0]


sumMa = sum(ma)
ans = 0
l, r = 0, n-1
for _ in range(n-1):
    a, b = 0, 0
    if ma[l] <= ma[r]:
        a = ma[l]
        l += 1
    else:
        a = ma[r]
        r -= 1

    b = sumMa -a
    ans += a * b 
    sumMa -= a

print(ans)
    