import sys
from collections import deque
input = sys.stdin.readline

'''
    1) 항상 오른쪽으로만 이동할 수 있다.
    2) i -> j로 갈 때 (j-i) * (1 + | A[i] - A[j] | ) 
    3) 한번 K만큼만 쓸수 있다.

'''

n, k = map(int, input().split())
ma = [0] + list(map(int, input().split()))
vi = [0] * (n+1)
q = deque()
q.append(1)
vi[1] = 1

while q:
    cn = q.popleft()
    
    for nn in range(cn+1, cn+k+1):
        if nn > n :
            break
        
        if vi[nn] == 1:
            continue


        if (nn - cn) * (1 + abs(ma[cn] - ma[nn])) <= k:
            
            if nn == n:
                print('YES')
                exit(0)

            vi[nn] = 1
            q.append((nn))

else:
    print('NO') 