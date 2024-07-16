import sys
input = sys.stdin.readline


ma =list(map(int, input().split()))
ma.sort()

a, b = 0,0 
a = ma[0] + ma[-1]
b = ma[1] + ma[2]
print(   abs(a - b))