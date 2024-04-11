#백준 주소 "https://www.acmicpc.net/problem/12784"
# (1) 양방향과 방문회수를 해주어야한다.
#     ㄴ> 이유 : 트리의 연결이 순차적이 확정이 아니기 때문 
#                 1 - 2, 3 | 2 - 4, 5 | 3 - 6, 7 
#                 이런식으로 순차적이 확정이라면 sort를 사용해서 들어가기만 하면 가능 
#             but 1 - 4, 5 | 4 - 2, 3 | 5 - 6, 7
#                 이라면 dfs로 들어가지 못할 수가 있음 
#                 양방향으로 묶어주어야 한다.

# (2) vi배열로 방문여부를 확인 
# (3) 말단 노드( leaf node )에는 무조건 부모 노드의 정보만 들어있음 
#     그렇기에 INF를 return

# (4) 돌아온 값과 그 노드로 가는 값을 비교 
#     만약 INF라면 말단 노드로 가는 가중치가 더해질 거다.

# (5) 이런식이라면 이전까지의 거리 <--- 다음 거리 
#     DAG가 성립한다.

# 시간 복잡도 계산 : O(TVE) 전체 노드와 엣지를 모두 살피기 때문 
#                           T = 테스트 케이스
                
#                  10^2 * 10^3^2 => 10^8 정도
import sys
input = sys.stdin.readline
INF = 2e9

def dfs(st):
    vi[st] = True
    tmp = 0
    for i in ma[st]:
        if not vi[i[0]]:
            tmp += min(i[1], dfs(i[0]))

    return tmp if tmp else INF


for _ in range(int(input())):
    n, m = map(int, input().split())
    
    if n == 1:
        print(0)
        continue
    
    ma = [[] for _ in range(n+1)]
    vi = [False] * (n+1)

    for _ in range(m):
        s, e, t = map(int, input().split())
        ma[s].append([e, t])
        ma[e].append([s, t])

    print(dfs(1))