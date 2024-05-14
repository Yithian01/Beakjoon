# M이 작기에 가능했던 방법
# 시간복잡도 계산 : n log n + n * m => O(nm) => 10^5정도
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = list(map(int, input().split()))

ma.sort(reverse=True)

cnt = 0

ans = [0] * m
for i in ma:
    tmp = 2e9
    idx = 0
    for j, v in enumerate(ans):

        if v < tmp:
            tmp = v
            idx = j
        
    ans[idx] += i


print(max(ans))
    