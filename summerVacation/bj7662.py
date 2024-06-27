from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 1e9

def checkPop(q, ma, isMin):
    while q:
        tmp = heappop(q)
        if ma[tmp[1]][1]:
            ma[tmp[1]][1] = False
            
            if isMin == 0:
                return -tmp[0]
            else:
                return tmp[0]
    return None


for _ in range(int(input())):
    n = int(input())
    uq, dq, cList = [], [], []
    for _ in range(n):
        a, b = map(str, input().rstrip().split())
        b = int(b)
        if a == 'I':
            heappush(dq, (b, len(cList)))
            heappush(uq, (-b, len(cList)))
            cList.append([b, True]) 
        
        else:

            if b == -1:
                checkPop(dq, cList, 1)
            
            else:
                checkPop(uq, cList, 0)

    

    ans = [0,0] #최대 최소 
    ans[1] = checkPop(dq, cList, 1)
    ans[0] = checkPop(uq, cList, 0)
    
    if ans[1] == None:
        print('EMPTY')
    elif ans[0] == None:
        print(ans[1], ans[1])
    else:
        print(*ans)
            