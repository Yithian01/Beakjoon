import sys
from collections import deque
input = sys.stdin.readline
'''
    A==B , B==C , A==C
    A!=B , B!=C , A==C

'''
def FIND(x):
    if vi[x] != x:
        vi[x] = FIND(vi[x])
    
    return vi[x]



n = int(input())
ma = [[] for _ in range(n+1)]
for _ in range(int(input())):
    s, a, b = map(str, input().split())
    a = int(a)
    b = int(b)

    ma[a].append((s, b))
    ma[b].append((s, a))

vi = [ _ for _ in range(n+1)]
for i in range(1, n+1):
    q = deque()
    num = [0] * (n+1)
    num[i] = 1

    for cs, cn in ma[i]:
        
        q.append((cs, cn, i)) # (E, 4, 1) <- 4는 1의 적이다.
        

    print(vi)
    while q:
        cs, cn, cb = q.popleft()  #친구여부, 현재, 이전
        
        for ns, nn in ma[cn]: # 친구여부, 다음
            if num[nn] == 1:
                continue

            num[nn] = 1
            if (cs == 'F' and ns == 'F') and (cs == 'E' and ns == 'E') : # 친구의 친구 
                a = FIND(cb)
                b = FIND(nn) 


                if a > b:
                    a, b = b, a

                if a != b:
                    vi[b] = a
                
            
            q.append((ns, nn, cn))


print(vi)