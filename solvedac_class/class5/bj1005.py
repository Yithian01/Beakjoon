# 프림, 크루스칼 대응 불가 --> 선행 노드가 여러개인 동시 진행이 가능하기 때문애 
# 진입 간선이 0인 노드를 찾아서 거기부터 dp를 진행한다.
# dp의 값은 해당 index까지 가는 최소거리 

# 즉 현재 노드 dp[i] = 선행 노드의 최소거리 dp[cn] + 현재 노드 값 
# 으로 나타낼 수 있음 

# 시간 복잡도 계산 : t * nm + nm => 10^3 * 10^5 => 10^8 정도
#                     1초까지 아슬아슬 할  것 같다.
from collections import deque
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, k = map(int, input().split())
    num = [0] + list(map(int, input().split()))
    ma = [[] for _ in range(n+1)] # i번째 노드 이후 이동하는 다음 노드
    id = [0] * (n + 1) # 진입 간선 개수
    dp = [0] * (n + 1) # 최소 신장 트리 (i번째 노드까지 가는 가장 최소 거리)

    for _ in range(k):
        s, e = map(int, input().split())
        ma[s].append(e)
        id[e] += 1
    
    q = deque()
    for i in range(1, n+1): 
        if id[i] == 0: # 진입 간선의 개수가 0개라면 시작점이라고 볼 수 있음 
            q.append(i)
            dp[i] = num[i]


    while q:
        cn = q.popleft()
        for i in ma[cn]:
            dp[i] = max(dp[i], dp[cn] + num[i])
            id[i] -= 1
        
            if id[i] == 0:
                q.append(i)

    ed = int(input())
    print(dp[ed])