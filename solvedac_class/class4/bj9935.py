# 원래 문자열 => ss , 폭발하는 문자열 => s  , 스택 => st 
# 1) 스택에 원래 문자열을 1개씩 넣는다. 
#     폭발하는 문자열의 길이가 될때까지 

# 2) 문자열이 폭발문자열이라면 폭발 문자열 길이만큼 pop해준다.
# 3) 마지막에 스택에 남아있으면 남은 문자열 출력 

# 시간 복잡도 계산 : 10^6 + 10^6정도 st에 모든 것을 넣다 빼었다 하기 때문에 
#                     O(N)
import sys
input = sys.stdin.readline


ss = input().rstrip()
s = input().rstrip()


st = []
cnt = len(s)
for i in range(len(ss)):
    st.append(ss[i])

    if ''.join(st[-cnt:]) == s:
        for _ in range(cnt):
            st.pop()


if len(st) == 0 :
    print('FRULA')
else:
    print(''.join(st))