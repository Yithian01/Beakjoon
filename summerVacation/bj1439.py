# 시간 복잡도 계산 : O(N)정도
import sys
input = sys.stdin.readline



s = input().rstrip()
a = [0] * 2
a[int(s[0])] += 1


for i in range(1, len(s)):
    if s[i-1] != s[i]:
        a[int(s[i])] +=1 

print(min(a))