from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
# 간선을 만들어 준 뒤 최소스패닝 트리를 만든다. MST 
# 이후 크루스 칼을 이용해서 MST 구현 

# 시간 복잡도 계산 : 3 n log n => 3 * 10^6 ~ 10^7 사이 + 3 * 10^5
n = int(input())

def FIND(a):
    if a != vi[a]:
        vi[a] = FIND(vi[a])
    return vi[a]


maA, maB, maC = [], [], []
for i in range(n):
    x, y, z = map(int, input().split())
    maA.append((x, i+1))
    maB.append((y, i+1))
    maC.append((z, i+1))
maA.sort()
maB.sort()
maC.sort()

ma = []
for s in maA, maB, maC:
    for i in range(1, n):
        cr, cn = s[i-1]
        nr, nn = s[i]
        heappush(ma, (abs(cr - nr), cn, nn) )
        
vi = [ _ for _ in range(n+1)]
ans = 0

while ma:
    we, st, ed = heappop(ma)
    
    a = FIND(st)
    b = FIND(ed)

    if a > b:
        a, b = b, a

    if a == b:
        continue
    
    vi[b] = a
    ans += we 


print(ans)