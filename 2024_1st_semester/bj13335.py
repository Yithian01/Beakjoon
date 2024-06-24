#pop을 하면 제일 앞의 것이 빠지는 것을 이용한다.
#길만큼의 배열을 만든다. q = [0] * (w)

#시간을 1씩 더해가면 다음 연산을 한다.
#q.pop(0) 제일 앞의 인수 제거 
#현재 sum(q)의 값 + 가야 할 트럭 ma[0] 가 L보다 작다면 추가 
#아니라면 q.append(0)

#시간출력

#시간복잡도계산: O(NM)
from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
ma = [0] + list(map(int, input().split()))

q = [0] * w
t = 0 

q = [0, 0]
q [0]

while q:
    q.pop(0)
    t += 1
    if ma:
        if sum(q) + ma[0] <= L:
            q.append(ma.pop(0))
        else:
            q.append(0)

    
print(t-1) # q[]가 0이 될 때도 반복하기 때문에