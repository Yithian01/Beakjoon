import sys
input = sys.stdin.readline


ta = {}

n = int(input())
for _ in range(2 *n - 1):
    s = input().rstrip()
    if s not in ta:
        ta[s] = 1

    else:
        ta[s] += 1

ans = ""
for k, v in ta.items():
    if v % 2 == 1:
        ans = k


print(ans)