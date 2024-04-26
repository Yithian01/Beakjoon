# n ~ m 까지 숫자를 문자열로 변환 
# 변환한 문자열을 int로 바꾸어서 0~9까지의 index값을 +1 씩 해가며 2개가 나오는지 확인 

# 시간복잡도계산 : tc * 5 * 10^3 * 4 * 4  => O(NM)
import sys
input = sys.stdin.readline


while True:
    try :
        n, m = map(int , input().split())
    except:
        break
    

    ans = 0 

    for i in range(n, m+1):
        isCheck = False
        num = [0] * (10)
        ss = str(i)
        for j in ss:
            num[int(j)] += 1
            if num[int(j)] >= 2:
                isCheck = True
                break

        if not isCheck:
            ans += 1        

    print(ans)