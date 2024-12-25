import sys
input = sys.stdin.readline
# 문제가 굉장히 불친절하다. 무슨 옮길 수 있다는 것을 명시를 해주지 않았다.
# UNION_FIND를 사용해서 다음에 오게 될 경우 한칸 씩 앞으로 땡겨주는 동작을 하게 된다.
# 그래서 현재 사용할 게이트가 FIND로 0일 경우 이제 더이상 앞으로 못당긴다는 것이다.

# 경로압축 기법 : FIND중에 NUM을 자동으로 변경해준다. <--- 시간 복잡도를 아낄 수 있다.

# 시간 복잡도 계산 : O(n) 정도
def FIND(x):
    if x != num[x]:
        num[x] = FIND(num[x])
    return num[x]


def UNION(a, b):
    a = FIND(a)
    b = FIND(b)

    if a > b:
        a, b = b, a
    
    num[b] = a



n = int(input())
m = int(input())

num = [ _ for _ in range(n + 1)]

ma = []
for _ in range(m):
    tmp = int(input())
    ma.append(tmp)

ans = 0
for i in ma:
    a = FIND(i)
    if a == 0:
        break


    UNION(a, a-1)
    ans += 1


print(ans)