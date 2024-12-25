import sys
input = sys.stdin.readline
INF = 10**9 + 1
# 누적합을 이용해야 한다. 3인조가 중간에 낄 경우를 대비해서 왼쪽에서의 누적합, 오른쪽에서의 누적합을 해야한다.
# 1) 정렬 후 자신의 바로 다음 사람과 짝을 지어야 최소인 것은 확정이다.
# 2) 1 (2 3 4) 5 일 경우 5-1 > 4-2 가 되기 때문에 3인조는 짝수번째 마다 반복한다.

# 시간 복잡도 계산 : n log n + n + n + n => 5 * 10^5 * 3 * 10 => 15 * 10^6 => O(10^7) 정도
# n = 5 * 10^5 



n = int(input())
ma = list(map(int, input().split()))
ma.sort()

le = [0] * n 
ri = [0] * n

for i in range(1, n, 2):
    le[i] = ma[i] - ma[i-1] 
    if i - 2 >= 0:
        le[i] += le[i-2] 

for i in range(n-2, 0, - 2):
    ri[i] = ma[i+1] - ma[i]
    if i + 2 < n:
        ri[i] += ri[i+2]


ans = INF
for i in range(0, n-2, 2):
    tmp = ma[i+2] - ma[i]
    if i - 2 >= 0:
        tmp += le[i-1]
    
    if i + 3 < n:
        tmp += ri[i+3]
    
    ans = min(ans, tmp)


print(ans)