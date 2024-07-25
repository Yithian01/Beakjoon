import sys
input = sys.stdin.readline


n, m = map(int, input().split())
ma = []
for i in range(1, n + 1):
    a = int(input())
    for _ in range(a):
        ma.append(i) 


for _ in range(m):
    a = int(input())
    print(ma[a])
