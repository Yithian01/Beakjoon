from collections import deque
import sys
input = sys.stdin.readline
ma = [-1] * (100002)

n, k = map(int, input().split())
q = deque()
q.append(n)


ma[n] = 0
while q:
    x = q.popleft()

    if x == k:
        break

    for nn in x-1, x+1, x * 2:
        if nn < 0 or nn >= len(ma):
            continue


        if ma[nn] > ma[x] + 1:
