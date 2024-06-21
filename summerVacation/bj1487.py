from heapq import heappush, heappop
import sys
input = sys.stdin.readline


q = []
for i in range(int(input())):
    a, b = map(int, input().split())
    if (a-b) < 0:
        q.append([-b, ])



print(f'q = {q}')
