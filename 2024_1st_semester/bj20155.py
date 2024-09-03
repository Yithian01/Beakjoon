import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = list(map(int, input().split()))

ans = {}
for i in ma:
    if i not in ans:
        ans[i] = 0

    ans[i] += 1

res = [0, 0]
for i in range(1, m + 1):
    if i in ans and res[1] < ans[i]:
        res = [i, ans[i]]

print(res[1])