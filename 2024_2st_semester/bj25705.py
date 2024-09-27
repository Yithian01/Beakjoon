# 시간복잡도 계산: O(NM + NM) -> 10^4 + 10^4

import sys
input = sys.stdin.readline
INF = 1e9

n = int(input())
ma = list(input().rstrip())
m = int(input())
res = list(input().rstrip())

for i in res:
    if i not in ma:
        print(-1)
        exit(0)


ans = 0
st = n-1
ed = 0
while ed  < m:


    st = (st + 1) % n
    if ma[st] == res[ed]:
        ed += 1

    ans += 1

print(ans)