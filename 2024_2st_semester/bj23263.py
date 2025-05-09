import sys
input = sys.stdin.readline
'''
    순서대로 쌓기 
    1 2 3 순으로 빼내기 stack?

'''
isTrue = False
n, m = map(int, input().split())
for _ in range(m):
    s = int(input())
    tmp = list(map(int, input().split()))
    for i in range(1, s):
        if tmp[i-1] < tmp[i]:
            isTrue = True
    

if isTrue:
    print('No')
else:
    print('Yes')
    