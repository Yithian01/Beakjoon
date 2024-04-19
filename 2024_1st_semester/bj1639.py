# (1) 모든 부분에서 <-- i --> 퍼져나가는 것을 확인 
# (2) 0 혹은 n보다 커질 때까지 오른쪽, 왼쪽의 숫자의 같은을 확인
# (3) (2)에서 오른쪽, 왼쪽이 같다면 현재 나아간 횟수 * 2가 좌우의 총 길이합

# 시간 복잡도 계산 : 50 * 50 => 25 * 10^2 => 2*10^3 => O(N^2)
import sys
input = sys.stdin.readline

n = input().rstrip()
m = len(n)

ans = 0
for i in range(m):
    we = 1
    cnt, res = 0, 0
    ri, le = 0, 0

    for j in range(i, -1, -1):
        k = j + we
        cnt += 1

        if j < 0 or k >= m:
            break

        le += int(n[j]) 
        ri += int(n[k])

        if le == ri:
            res = cnt * 2
        we += 2

    ans = max(ans, res)
print(ans)