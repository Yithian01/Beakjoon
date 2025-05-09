import sys
input = sys.stdin.readline

'''
    구성이 같고 순서가 다른 쌍은 배제 --> 조합 
    TIME LIMIT : 2 * 10^8 

    각 우주의 행성 순서가 중요 
    1 :  1  3  2
    2 : 12 50 31

    1 <  3   3 >  2   1 <  2
   12 < 50  50 > 31  12 < 31 


    10^2 * 10^4 = 10^6
    각 크기의 순서를 매기고 같으면 동일한 쌍으로 묶어준다.


    파이썬은 "문자열+" 과 join 함수랑은 시간복잡도 차이가 난다. =>
    --> 문자열이 불변이다. "a" + "b" = 새롭게 A,b 를 만들어 낸다. 
     
'''
n, m = map(int ,input().split())
ma = [[] for _ in range(n)]
ta = []

for i in range(n):
    for j, v in enumerate( map(int, input().split()) ):
        ma[i].append([v, j])
    

    ma[i].sort(key= lambda x: x[0])

    for j in range(1, m):
        if ma[i][j][0] == ma[i][j-1][0]:
            ma[i][j][1] = ma[i][j-1][1]

    ta.append(' '.join([str(j[1]) for j in ma[i]]))



ans = 0
for i in range(n- 1):
    for j in range(i+1, n):
        if ta[i] == ta[j]:
            ans += 1


print(ans)