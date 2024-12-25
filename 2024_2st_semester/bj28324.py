import sys
input = sys.stdin.readline

#   3 2 1 5
# 0 3 2 1 1 0
# 뒤에 부터 확인 

ans = 0 
n = int(input())
ma = list(map(int, input().split()))
ma[-1] = 1
for i in range((n-2), -1, -1):
    if ma[i] >= ma[i+1] + 1:
        ma[i] = ma[i+1] + 1


print(sum(ma))