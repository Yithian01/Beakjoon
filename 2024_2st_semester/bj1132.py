import sys
input = sys.stdin.readline

'''
    1) A ~ J 까지 총 10개 가 있다면 누군가는 0을 맞아야 함 
    2) 각 자리수별로 숫자와, 제일 앞에 오는 것에 True로 표시 해줌( 0 이 될 수 없음을 표시 ) 
    3) 큰 수대로 정렬 후 맨 뒤가 if 0이 될수 없다면 제일 작은 수의 값을 제외해준다.

    --> 각 idx가 A인지 B인지는 중요하지 않다. 각 자리수가 더 중요하기 때문에

    시간 복잡도 계산: O(1)

'''

ma =[[0, False] for _ in range(10)] ## 각 idx는 A ~ J를 의미함, 가자의 자릿값과 0이 될수 있음, 없음을 나타냄 
for _ in range(int(input())):
    s = input().rstrip()
    cnt = 1

    ma[ord(s[0]) - ord('A')][1] = True
    for i in range(len(s)-1, -1, -1):
        ma[ord(s[i]) - ord('A')][0] += cnt 
        cnt *= 10


ma.sort(reverse=True)

if ma[9][1]: # 만약 등장한 글자가 9글자 이하라면 마지막 배열은 무조건 False다.
    for i in range(8, -1, -1):
        if not ma[i][1]:
            del ma[i]
            break
    

cnt = 9
ans = 0
for i in range(9):
    ans += ma[i][0] * (cnt - i) #  효율적인 식이다. 어차피 자리수가 안나온 수들은 0이므로 곱해봤자 0이다.

print(ans)