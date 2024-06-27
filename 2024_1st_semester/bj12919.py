# s -> t로 가는 시간 복잡도는 2^n이기에 시간초과
# t -> s로 가는 것을 계산 갈 수 없는 조합이면 자동으로 푸르닝 가능
# 시간복잡도 계산: O(N)정도
import sys
input = sys.stdin.readline


def bt(ss):
    
    if ss == s:
        print(1)
        exit(0)
    
    if len(ss) == 0:
        return 0
    
    if ss[-1] == 'A':
        bt(ss[:-1])

    if ss[0] == 'B':
        bt(ss[1:][::-1])


s = input().rstrip()
t = input().rstrip()

bt(t)
print(0)