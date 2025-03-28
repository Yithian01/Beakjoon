import sys
input = sys.stdin.readline


def GDC(a, b):
    tmp = 0 
    while b != 0:
        tmp = a % b
        a = b 
        b = tmp
    return a


def LCM(a, b):
    return int( a * b // GDC( a, b ) ) # <---- / 를 //로 해줘야 통과 뭔소리야 


n = int(input())
ma = list(map(int, input().split()))

m = ma[0]
for i in range(1, n):
    m = LCM(m, ma[i])

ans = [m, 0] # 분모/분자
for i in range(n):
    ans[1] += (m // ma[i])

gcd = GDC(ans[0], ans[1])
print( f'{ans[0] // gcd}/{ans[1] // gcd}')