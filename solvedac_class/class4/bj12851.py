# BFS
# 주의 사항 
# (1) 1 --> 2로 가는 것은 +1, *n 둘다 가능 
#         * 그렇기에 가중치가 같은 장소도 최소힙에 넣어줘야한다.

# (2) 최소거리 메모리제이션 
#         * 정답이어도 최소거리를 지키지 못했다면 CUT
#           최소거리와 같다면 +1 
#           더 작은 거리라면 가중치 초기화, 횟수 초기화

# 시간복잡도 계산 : O(3 * n)정도
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = 2e9
maxLen = 100001 

n, m = map(int, input().split())
if n == m :
    print(0)
    print(1)
    exit(0)


ma = [INF] * maxLen
ma[n] = 0

q = []
heappush(q, (0, n))

ans = INF
mVal = INF
while q:
    w, cn = heappop(q)
        
    for i in [-1, 1, 2]: 
        if i == 2:
            nn = cn * 2
        else:
            nn = cn + i

        if nn < 0 or nn >= maxLen:
            continue

        if nn == m and mVal >= w + 1:
            if mVal > w + 1:
                mVal = w + 1
                ans = 1

            else:
                ans += 1
        

            
        if ma[nn] >= ma[cn] + 1 :        
            if ma[nn] > ma[cn]:
                ma[nn] = ma[cn] + 1
            heappush(q, (w + 1, nn))

        
                

print(ma[m])
print(ans)
