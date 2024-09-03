# pypy로 하면 터진다. 
# 추가적인 메모리 사용하고 시간 복잡도를 감소시키기 때문에

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


# 특별상 1명이면 그사람 
# 정사각형으로 나눠서 재귀로 구역마다 4명 
# 네명 중 추첨번호 두 번째로 작은 사람이 뽑힌다.

n = int(input())
ma = [list(map(int, input().split())) for _ in range(n)]


def bt( cnt, r, c):
    if cnt <= 1:
        return ma[r][c] 
    
    tmp = cnt // 2 
    q = []
    q.append(bt(tmp, r, c))
    q.append(bt(tmp, r + tmp, c))
    q.append(bt(tmp, r, c + tmp))
    q.append(bt(tmp, r + tmp, c + tmp))

    q.sort()
    return q[1]

print(bt(n, 0, 0 ))