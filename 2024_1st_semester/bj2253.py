from collections import deque
import sys
input = sys.stdin.readline


se = set()
n, m = map(int, input().split())
ma = [[] for _ in range(n+1)]
for _ in range(m):
    s = int(input())
    se.add(s)
    
def sol():
    q = deque()
    q.append((1,0,0)) # 현재위치, 스피드, 점프횟수

    while q:
        cn, sp, jp = q.popleft()
        for nsp in [sp-1, sp, sp+1]:
            if nsp <= 0 : continue
            nn = cn + nsp

            if nn == n:
                return jp+1
            if nn < n and nn not in se and nsp not in ma[nn]:
                ma[nn].append(nsp)
                q.append((nn, nsp, jp+1))

    return -1

print(sol())