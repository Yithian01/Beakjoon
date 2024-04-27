'''주소 : https://www.acmicpc.net/problem/2740'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]

nn, mm = map(int,input().split())
b = [list(map(int, input().split()))for _ in range(nn)]

ans = [[0] * mm for _ in range(n)]

for r in range(n):
    for c in range(mm):
        tmp = 0
        for i in range(m):
            tmp += a[r][i] * b[i][c]

        ans[r][c] = tmp

for r in ans:
    print(*r)