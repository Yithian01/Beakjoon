'''주소 : https://www.acmicpc.net/problem/10830'''
import sys
input = sys.stdin.readline
INF = 1000000007

def mul(a, b):
    nn = len(a)
    mm = len(b[0])
    c = [[0] * mm for _ in range(nn)]
    
    for i in range(nn):
        for j in range(mm):
            tmp = 0
            for k in range(2):
                tmp += a[i][k] * b[k][j]
            c[i][j] = tmp % INF

    return c

def divid(a, cnt):
    if cnt == 1:
    
        return a        

    
    tmp = divid(a, cnt // 2)
    if cnt % 2 != 0:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    

n = int(input())
A = [[1,1], [1,0]]

C = divid(A, n)
D = mul(C, [[1],[0]])

print(*D[1])