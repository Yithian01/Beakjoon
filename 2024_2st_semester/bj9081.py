from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# 사전 순으로 앞선다는 뜻 

for _ in range(int(input())):
    s = list(input().rstrip())
    
    tmp = s[-1]
    cnt = len(s)-1
    for i in range(len(s)-2, -1, -1):
        tmp = []
        for j in range(i, len(s)):
            if ord(s[i]) < ord(s[j]):
                heappush(tmp, (s[j], j))

        if len(tmp) > 0:
            diff, k = heappop(tmp)
            s[k] = s[i]
            s[i] = diff 

            s[i+1:] = sorted(s[i+1:])
            break

    print(''.join(s))