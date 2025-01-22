import sys
input = sys.stdin.readline
INF = 1000000007

ma = [1] * 51
ma[2] = 3

for i in range(3, 51):
    ma[i] = (ma[i-2] + ma[i-1]  +1 )% INF

n = int(input())
print(ma[n])