# 윈도우 슬라이딩
# 대문자와 소문자를 모두 사용하기 위한 배열 60개를 생성 
# wa = 원본 문자열 정답배열
# sa = 윈도우 슬라이딩 사용할 배열 

# 1) 입력받은 배열을 원본 글자의 길이가 될 때까지 
#    순서대로 그 글자 -65에 해당하는 배열의 인덱스에 + 1

# 2) 원본 문자열과 길이가 같아졌다면 wa와 sa의 값들이 모두 같은지 확인한다.
# 3) 같다면 ans + 1 그 후 시작 인덱스를 가르키는 st에 해당하는 sa 배열의 값을 -1

# 4) st + 1  -> 다음에 제거해줄 인덱스 

# 시간 복잡도계산 : 3 * 10^3 + 3 * 10^6 => O(N+M)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w = input().rstrip()
s = input().rstrip()

wa = [0] * 60 
sa = [0] * 60 


ans = 0
st, ed = 0, 0

for i in w:
    wa[ord(i) - 65] += 1


for i in range(len(s)):
    sa[ord(s[i]) - 65] += 1
    ed += 1

    if ed == n:
        
        if wa == sa:
            ans += 1
        
        sa[ord(s[st])- 65] -= 1
        st +=1
        ed -= 1

print(ans)