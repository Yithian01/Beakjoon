# inComeNode를 처리하며 1 ~ 각 노드까지의 최대거리를 업데이트 하며 시작
# 1번 노드에서 가는 부분을 먼저 처리하고 inComeNode가 0인 곳울 dq에 넣어서 시작
# 각 노드들은 자기에게 들어오는 최대 거리인 노드를 가지고 있음 

# 시간 복잡도 계산: O(VE) -> 간선만큼 보게 되고 각 노드를 방문하므로 VE다.
from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
m = int(input())

ma = [[] for _ in range(n+1)] # 간선 정보 저장 동적 배열
inCome = [0] * (n+1) # 들어오는 간선 개수
ans = [(-1,-1) for _ in range(n+1)] # 노드에 들어오는 최대거리와 노드
dq = deque()

for _ in range(m):
    s,e,w = map(int,input().split())
    ma[s].append((e,w))
    inCome[e] += 1

for e, w in ma[1]:
    ans[e] = (w, 1)
    inCome[e] -= 1
    if inCome[e] <= 0: # 1에서 시작한다는 조건이 있기에 여기에 두었음 
        dq.append(e)
    

while dq:
    cn = dq.popleft()
    cw, _ = ans[cn] # 현재 노드까지 오는데 최대 거리

    if cn == 1:
        break

    for nn, w in ma[cn]:
        nw = cw + w # 다음 노드까지의 거리 
        
        if ans[nn][0] < nw:
            ans[nn] = (nw, cn) # 거리, 이전 노드 업데이트
    
        inCome[nn] -= 1

        if inCome[nn] <= 0:
            dq.append(nn)
        



def bt(cn, cnt):
    if cn == 1:
        print(1, end=' ')
        return
    bt(ans[cn][1], cnt + 1)
    print(cn, end=' ')
    if cnt == 0:
        print(1, end=' ')


# ans에는 자기에게 들어오는 노드가 있음 즉 거꾸로 
# 1로 돌아오므로 1로 들어오는 노드를 넣어서
# 다시 1이 나올 때까지 그 숫자를 넣어주고 자기 숫자 출력 
print(ans[1][0])
bt(ans[1][1], 0)