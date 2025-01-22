import sys
input = sys.stdin.readline
INF = 10001

ans = INF 
n, m, k, l = map(int, input().split())
for _ in range(k):
    price = int(input())
    ma = list(map(int, input().split()))
    for i in ma:
        if n <= i and price < ans:
            ans = price


if m >= ( ans * n):
    print( ans * n)
else:
    print("stay home")
