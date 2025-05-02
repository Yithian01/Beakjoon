from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
    1) 도둑은 1부터 시작 // 경찰은 노드를 막는 게 아니라 가는 간선을 막는다.
    2) N번째 노드에 접근하는 간선이 1라면 불가능 -1 출력 

    가중치는 항상 양의 정수 
    다익스트라 사용: 시간복잡도 O(V+E)V 
    V = 10^3
    E = 5 * 10^3

    n에 오는 결과만 보면?
'''

n, m = map(int, input().split())

ma = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    ma[a].append((b, t))
    ma[b].append((a, t))


ans = [INF, 0] # min, max 값

for i in range(n):
    if i == 1:
        continue

    dp = [INF] * (n+1)
    dp[1] = 0
    
    q = deque()
    q.append((1, 0))

    while q:
        
        cn, cw = q.popleft()

        for nn, dw in ma[cn]:
            if nn == i:
                continue

            if dp[nn] > cw + dw:
                dp[nn] = cw + dw
                q.append((nn, cw + dw))

    
    if dp[n] == INF:
        print(-1)
        exit(0)
    

    ans[0] = min(ans[0], dp[n])
    ans[1] = max(ans[1], dp[n])

print(ans[1] - ans[0])
