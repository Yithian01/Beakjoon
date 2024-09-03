# 나중에 뛰는 경우가 좋은 경우가 있음 
# vi가 아닌 해당 배열에 온 경우의 수를 보는 q를 사용

# 시간 복잡도 계산: 20 * 20 * 3 => 120 => 10^2승 정도

from collections import deque
import sys
input = sys.stdin.readline
INF = 2e9
dq = deque()

n = int(input())
q = [[] for _ in range(n+1)]
we = [[0,0,0,0] for _ in range(n+1)]

for i in range(1, n):
    a, b = map(int,input().split())
    we[i][1] = a
    we[i][2] = b

k = int(input())
for i in range(1, n):
    we[i][3] = k


ans = INF
dq.append( (1, 0, 0) ) # 현재위치, 점프여부, 현재가중치
while dq:
    cn, jump, cw = dq.popleft()

    if cn == n:
        ans = min(ans, cw)


    for dr in range(1, 4):
        if jump == 1 and dr == 3:
            continue

        nn = cn + dr
        if nn > n:
            continue

        if (cn, jump, cw) not in q[nn]: 
            q.append((cn,jump, cw))
            tmp = 0
            if dr == 3:
                tmp = 1
            dq.append((nn, jump + tmp, cw + we[cn][dr] ))


print(ans)