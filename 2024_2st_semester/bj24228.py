import sys
input = sys.stdin.readline


n, m =map(int, input().split())
ans = m * 2 + (n-1)


print(ans)