# 다각형의 넓이 => 벡터의 외적의 공식으로 꼭짓점이 순서대로 주어지면 쉽게 구할 수 있다.

import sys
input = sys.stdin.readline

n = int(input())

rq, cq = [], []

for _ in range(n):
    c, r = map(int, input().split())
    rq.append(r)
    cq.append(c)


rq.append(rq[0])
cq.append(cq[0])


# r -> c  , c -> r
rc, cr = 0, 0 
for i in range(n):
    cr += cq[i] * rq[i+1]
    rc += rq[i] * cq[i+1]

ans = abs(rc - cr)
print(ans /2 )