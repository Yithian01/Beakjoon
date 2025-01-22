import sys
input = sys.stdin.readline

# 최악의 경우는 n -1번을 뺴야한다.
# 현재 인덱스( 최고값 )에서 0까지 보면서 target을 찾는다 초기target은 n-1 
# ans = 변경하지 않아도 되는 값 

# 시간 복잡도 계산 : O(n)
n = int(input())
m = [int(input()) for _ in range(n)]

ans = 1
st = 0
for idx, val in enumerate(m): 
    if val == n:
        st = idx
        break

target = n - 1
for i in range(st - 1, -1, -1):
    if m[i] ==  target:
        ans += 1
        target -= 1

print(n - ans)