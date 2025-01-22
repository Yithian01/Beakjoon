from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

ans = 0
n, m, k = map(int, input().split())
ma = [[] for _ in range(n+1)]
ta = {} # 각 지지대 별 펭귄까지 최소 개수, 지지대
for i in range(1, m + 1):
    ta[i] = (0, 0) # 개수, 지지대


for _ in range(n -1):
    st, ed = map(int, input().split())
    ma[st].append(ed)
    ma[ed].append(st)


# 1) 펭귄과 연결된 지지대 찾기 
# 2) (1)에서 주요 지지대 까지 경로 찾기 
# 3) 가장 짧은 경로가 정답 
vi = [False] * (n+1)
q = deque()
for i in range(1, m + 1):
    q.append((i, i,  1))
    vi[i] = True

while q:
    cn, st,  cw = q.popleft()

    for nn in ma[cn]:

        if nn == k:
            if ta[st][1] == 0:
                ta[st] = (cw, 1)

            else:
                ca, cb = ta[st]
                ta[st] = ((ca + cw -1), cb + 1)
            continue

        if not vi[nn]:
            vi[nn] = True
            q.append((nn, st, cw + 1))



# (1, 1, 2) <-- 1번은 1개의 지지대 2개 차지 
# (3, 2, 3) <-- 3번은 2개의 지지대 3개 차지
res = list( ta.items())
res.sort(key=lambda x : x[1][0])

ans = [INF,0] # 개수, 지지대 개수
for _, val in res:
    if val[0] == 0:
        continue

    

    if val[1] >= 2 and ans[0] >= val[0]: # 똑같은 개수라면 하나가 이득이다.
        ans = [val[0], val[1]]
        break

    if ans[1] >= 2:
        break

    else:
        if ans[1] == 0: # 처음이라는 뜻 
            ans = [val[0], 1]
        
        else: 
            ans[0] += val[0] 
            ans[1] += 1

print(n - (ans[0] + 1))