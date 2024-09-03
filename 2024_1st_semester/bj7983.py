import sys
input = sys.stdin.readline


# n개의 과제 
# 과제 i = d일을 t일 안에 끝내기 
# 한번 시작 시 계속함
ma = [[0, 0]]
n = int(input())
for _ in range(n):
    d, t = map(int, input().split())
    ma.append([t, d])

ma.sort(key = lambda x : x[0], reverse=True)
ans = 0
for i in range(n):
    # 현재 t, d 와 그 이전 t, d를 비교 
    ct, cd = ma[i]
    tmp = ct - cd  
    if ma[i+1][0] >= tmp:
        ma[i+1][0] = tmp

ans = ma[n-1][0] - ma[n-1][1]
print(ans)