import sys
input = sys.stdin.readline


def cal(i, k):
    tmp = 0
    tmp += i // k
    if i % k != 0:
        tmp += 1

    return tmp

# 1~2학년 구분 없음
# 3~6학년 남/여 구분

# 1~2 ///  3 ~ 4 //// 5 ~ 6
a = 0
b = [0,0] # 여자, 남자
c = [0,0]

n, k = map(int, input().split())
for _ in range(n):
    # s = 0(여자)1(남자) 
    s, y = map(int, input().split())
    if y <= 2:
        a += 1
    elif y <= 4:
        b[s] += 1
    
    else:
        c[s] +=1
    
ans = 0 
ans += cal(a, k)
ans += (cal(b[0], k) + cal(b[1], k))
ans += (cal(c[0], k) + cal(c[1],k))

print(ans)