# 최대값을 구하고 그 인덱스부터 끝까지 계속해서 초기화해준다.

# 시간 복잡도 계산: 2*10^2 * 10^2 log 10^2 * 10^2 => 2 * 10^7정도 
from collections import deque
import sys
input = sys.stdin.readline


def findMaxVal(tx, ty):
    x = tx
    y = ty
    
    
    while True:
        mx = max(x)
        my = max(y)

        if mx == -1 or my == -1:
            break
        
        ix = x.index(mx)
        iy = y.index(my)

        if mx == my:

            return [ix, iy]
        elif mx > my:
            
            x[ix] = -1
        else:
            y[iy] = -1

    return [-1,-1]

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

q = deque()

while a and b:
    
    res = findMaxVal(a, b)
    if res[0] == -1:
        break
    
    else:
        tmp = a[res[0]]
        q.append(tmp)
        a = a[res[0]+1:]
        b = b[res[1]+1:]
        

print(len(q))
if len(q) != 0:
    print(*q)
