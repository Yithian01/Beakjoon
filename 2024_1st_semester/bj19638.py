# (1) t초 안에 ma안에 모든 수가 m보다 작아야 한다.
# (2) 1은 줄이지 못한다.
# (3) t초 내에 성공하면 YES, 최소횟수
# (4) t초 내에 줄이지 못하면 NO, 그 때에 최대값

# 최대힙을 이용하면 항상 배열의 최대값을 알 수 있다.
# 최대값이 1이거나 m보다 작다면 줄이지 않아도 된다.
# 최대힙의 가장 위가 m보다 작거나 1일 때까지 배열의 값을 줄이고 넣어준다.

# 최대힙의 가장 위가 m보다 작을 경우 힙안에 모든 수가 m보다 작음이 보장된다.-- YES
# 최대힙의 가장 위가 m보다 크거나 같은 경우 적어도 1개 이상이 m보다 크다. -- NO

# 시간복잡도 계산:   10^5 log10^5 => 2*10^6 ---->  O(tlog(n))
#                    t번 만큼 (  heap정렬 시 log n만큼 ) 
from heapq import heappush, heappop
import sys
input = sys.stdin.readline


q = []
n, m, t = map(int, input().split())
for _ in range(n):
    a = int(input())
    heappush(q, -a)

ans = 0
cnt = 0
while t:
    t -= 1
    cnt += 1

    if -q[0] < m or -q[0] <= 1:
        break

    cn = -heappop(q)
    if cn < m: # m보다 크면서 1보다 크면 
        ans = max(ans, cnt) # 현재가 줄인 것중 가장 큰것 

    cn //= 2
    heappush(q, -cn)
    ans = max(ans, cnt)

if -q[0] >= m:
    print('NO')
    print(-q[0])
else:
    print('YES')
    print(ans)
        