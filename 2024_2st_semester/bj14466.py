import sys
input = sys.stdin.readline
dir = [(0, 1),(0, -1),(1, 0),(-1, 0)]


N, K, R = map(int, input().split())
n = (N * (N-1) + (N-1)) + 1
ma = [[-1] * n for _ in range(n)]
    

for _ in range(R):
    sr, sc, er, ec = map(int, input().split()) 
    sr, sc, er, ec = sr-1, sc-1, er-1, ec-1

    st = N * sr + sc
    ed = N * er + ec
    ma[st][ed] = 1
    ma[ed][st] = 1


res = []
for _ in range(K):
    r, c = map(int, input().split())
    r, c = r-1, c -1
    res.append( N * r + c)
    
ans = 0 
for i in range(len(res) -1):
    for j in range(i+1, len(res)):
        if ma[res[i]][res[j]] == 1:
            ans += 1

print(ans)

