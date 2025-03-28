import sys
input = sys.stdin.readline


# 길이를 본다면?
s = input().rstrip()
n = int(input())
ma = []
ans = [[] for _ in range(n)]

for _ in range(n):
    tmp = input().rstrip()
    m = len(tmp) - 1 

    ma.append((m, tmp))

ma.sort(key=lambda x : x[0])

for k in range(len(s)): # 범위
    for i in range(len(s)): # 시작 위치
        if i + k + 1 > len(s):
            break

        a = s[i:i+k+1]
        print(k, a)
        for idx, tmp in enumerate(ma):
            if tmp[0] == k and a == tmp[1]:
                
                ans[idx] = [i, i+k]

ans.sort(key=lambda x : x[1])
print(ans)

