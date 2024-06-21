#모든 조합을 볼수 있는 정도의 n값이다. NPN => n!이므로 볼 수 있다.

#시간 복잡도 계산: O(n!)
from itertools import permutations
import sys 
input = sys.stdin.readline


n = int(input())
ma = list(map(int, input().split()))


ans = 0
for i in permutations(ma, n):
    q = [0] + list(i) # 튜플 반환이라 list로 바꿔주어야 한다.
    sq = [0] * (n+1)

    for j in range(1, n+1):
        sq[j] = sq[j-1] + q[j]

    cnt = 0
    for k in range(n):
        for l in range(k+1, n):
            if sq[k] + 50 == sq[l]:
                cnt += 1

    ans = max(ans, cnt)

print(ans)