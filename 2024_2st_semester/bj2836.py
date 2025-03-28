from heapq import heappush, heappop
import sys
input = sys.stdin.readline


# cn에서 다음에 갈 곳보다 가깝다면 거기를 가는 것이 이득
# 타야하는 곳과 아닌 곳을 잘 봐야 함 먼저 타야 내릴 수 있음

iq, oq = [], [] #
cn = 0
ans = 0


n, m = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(n)]
ma.sort()

heappush(oq, m)
for st, ed in ma: 
    if abs(cn - st) < abs(oq[0] - cn):
        ans += abs(st - cn)
        cn = st 
        heappush(oq, ed)

    else:
        nn = heappop(oq)
        ans += abs(cn - nn)
        cn = nn 
        heappush(oq, st)    
        heappush(oq, ed)    

while oq:
    print(f'현재 ans = {ans}')
    nn = heappop(oq)
    ans += abs(nn - cn)
    cn = nn

print(ans)