import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

'''
    최단 거리 알고리즘 = 다익스트라 O(N+V)

    각 위치에서 모든 위치 계산 = 플로이드 워샬 O(N^3)
        500 * 500 * 500 => 125 * 10^6 => 1*10^8 제한시간 2초라 가능할 듯 


    
'''

n, m = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(n)]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k :
                continue

            if ma[i][k] and ma[k][j]:
                ma[i][j] = min(ma[i][j], ma[i][k] + ma[k][j])


for _ in range(m):
    a, b, c = map(int, input().split()) # 현재위치, 다음위치, 시간
    a -= 1
    b -=1
    # 시간안에 a->b 가능한지 여부 확인 

    if ma[a][b] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')
