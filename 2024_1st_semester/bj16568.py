# 0 - 1 BFS
# (1) a, b번 앞으로 간다는 것은 a+1번째가 된다는 것이다.
# (2) 추가로 1도 넣어주어야 한다. 자연스럽게 기다리는 것은 1초이기 때문
# (3) 가중치는 단순히 한번 가는 경우 a, b, (순서 기다리기 = 1) 밖에 없기에 0-1BFS 가능하다.

# 시간 복잡도 계산 : n보다 작아질 수는 없다. O(N)
import sys
input = sys.stdin.readline
INF = 2e9

n, a, b = map(int,input().split())
ma = [INF] * (n+1)
ma[n] = 0

if n <= 1:
    print(n)
    exit(0)

q = [n]
while q:
    tmp = []
    for i in q:
        for j in [a+1,b+1,1]:
            if (i-j) < 0 :
                continue
        
            if ma[i-j] > ma[i] +1:
                ma[i-j] = ma[i] + 1
                tmp.append((i-j))
    q = tmp

print(ma[0])