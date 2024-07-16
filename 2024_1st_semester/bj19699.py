from itertools import combinations
import sys
input = sys.stdin.readline
# 10000까지의 소수로 넉넉잡자


prime = [1] * 10001
prime[0], prime[1] = 0,0
for i in range(2, 10001):
    if i > 9001:
        break

    if prime[i] == 0 :
        continue

    j = 2
    while i * j < 9001:
        prime[i*j] = 0
        j += 1
    



n, m = map(int, input().split())
ma = list(map(int, input().split()))

ans = []
for com in combinations(ma, m):
    tmp = sum(list(com))
    if prime[tmp] == 1:
        ans.append(tmp)
        prime[tmp] = 0

if len(ans) == 0 :
    print(-1)
else:
    ans.sort()
    print(*ans)
