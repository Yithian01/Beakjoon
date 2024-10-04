# 예제를 가지고 설명 
# 1 2 3 4 5 6 7
# 3 1 3 7 3 4 6
# -----------------
# 
# DFS를 돌려서 사이클의 시작점 ~ 마지막 개수를 ans에 더해주고 n - ans를 해준다.
# 1 ~ N으로 시작
# Cycle = [] -->   1 --> 3 -- 3 이 나오면 3을 넣지 않고  3 ~ 마지막배열까지 의 길이 => 1
# Cycle = [] -->   2 --> 1인데 1은 방문했지만 현재 싸이클에 없으므로 return 
# Cycle = [] -->   3 --> 3은 방문함
# Cycle = [] -->   4 --> 7 --> 6 ---> 4가 나오고 4,7,6 즉 3개의 값을 ans에 더하기 
# Cycle = [] -->   5 --> 3은 방문함
# 이후 모두 방문함 

# ans => 1 + 3 => 4 고 7 - 4 = 3을 만족함 

#시간 복잡도계산 : 결국 모두 방문한므로 -> 10^5 + 10^5 정도
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def DFS(cn):
    global ans

    vi[cn] = True
    cycle.append(cn)
    nn = ma[cn]

    if vi[nn]:
        if nn in cycle:
            ans += len( cycle[cycle.index(nn): ])
    else:
        DFS(nn)


for _ in range(int(input())):
    n = int(input())
    ma = [0] + list(map(int, input().split()))
    vi = [False] * (n+1)


    ans = 0
    for i in range(1, n+1):
        if not vi[i]:
            cycle = []
            DFS(i)

    
    print(n - ans)