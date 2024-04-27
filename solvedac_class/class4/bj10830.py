'''주소 : https://www.acmicpc.net/problem/10830'''
import sys
input = sys.stdin.readline

def mul(a, b):
    c = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += a[i][k] * b[k][j]
            c[i][j] = tmp % 1000

    return c

def divid(a, cnt):
    if cnt == 1:
        
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000

        return a        

    
    tmp = divid(a, cnt // 2)
    if cnt % 2 != 0:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

C = divid(A, m)

for i in C:
    print(*i)