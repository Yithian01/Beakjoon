# ma => 2차원 배열, 연결된 정보 담고 있음 
# dist => 자신에게 오는 최단 노드의 정보를 담고 있음 
# vi => 자신에게 오는 최단 거리 저장

# 시간 복잡도 계산: 10^3 * 10^5 => 10^8
from heapq import heappush, heappop
from collections import defaultdict 
import sys
INF = int(2e9)

n = int( sys.stdin.readline().rstrip())
m = int( sys.stdin.readline().rstrip())

ma = defaultdict(list)
for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    ma[s].append((t, e))
st, ed = map(int,  sys.stdin.readline().split())

dist = [0] * (n+1)
vi = [INF] * (n+1)

def BFS(st):
    vi[st] = 0
    q = []
    heappush(q, (0, st))
    while q:
        w, cn = heappop(q)
        if vi[cn] < w: continue

        for t, nn in ma[cn]:
            cost = w + t
            if cost < vi[nn]:
                vi[nn] = cost
                dist[nn] = cn
                heappush(q, (cost, nn))

BFS(st)
print(vi[ed])

ans = [ed] 
a = ed

while a != st:
    ans.append(dist[a])
    a = dist[a]
    
ans = ans[::-1]
print(len(ans))
print(' '.join(map(str, ans)))