import sys
input = sys.stdin.readline
# 팩토리얼에서는 모든 10을 구성하는 
# 5와 2 중 5의 개수가 항상 더 적기 때문에,
# 끝에 있는 0의 개수는 곧 5의 개수에 의해 결정

# 즉 0의 개수가 3일 경우 000 이므로 5를 세번이 나오는 가장 작은 경우를 찾아야 한다.
# 1 ~ 15! 사이에 3이 3개가 되는 경우를 찾는 것 

# 0의 개수가 5개일 경우 
# 5는 6개가 곱해진다. 즉 이럴 경우 2가 5보다 많이 나오므로 6개가 곱해지면 0의 개수가 6개가 된다.

# 시간 복잡도 계산 :   O(log5(n)
def FIND_FIVE(x):
    cnt = 0 
    while x >= 5:
        cnt += x // 5
        x //= 5
    
    return cnt

n = int(input())
st, ed = 0, n * 5  # 열림 닫힘

while st +1 < ed:
    mid = (st + ed) // 2

    tmp = FIND_FIVE(mid)
    
    if tmp < n:
        st = mid
    
    else:
        ed = mid

if FIND_FIVE(ed) == n :
    print(ed)

else:
    print(-1)