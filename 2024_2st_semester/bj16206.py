import sys
input = sys.stdin.readline

'''
 10으로 나눴을 경우 몫이 2이상이면 20이므로 1번 자를 수 있음 
 몫   :   1  2  3  4  5
 횟수 :   0  1  2  3  4
 ------------
 ** 길이가 10인 것만 먹는다 

    
 dp로는 풀리지 않느다.
 이유 : 60의 경우 1번,2번,3번 ... 5번 자르는 모든 경우를 살펴봐야 하므로 불가능

 그리디로 가능 
 1) 10으로 나눴을 때의 나머지가 작은 순서대로 정렬
 2) 10으로 나눴을 때 나머지가 없다면 배수라는 뜻 
    배수는 20 -> 1번 자르고 2개가 나온다.
    
    2-1) 자를 수 있는 경우가 m보다 크다면 m개 만큼만 ans에 더한다.
    2-2) 자를 수 있는 경우가 m보다 작거나 같다면 ans += 개수

 3) 나머지가 있는 경우는 23 -> 2번 자르고 2개가 나온다.

    3-1) 자르는 경우가 m보다 크면 ans += m
    3-2) 자르는 경우가 m보다 같거나 작으면 개수를 +해준다.

 4) m - tmp 를 해준다.

 시간복잡도 계산: O(nlogn + n) 

 '''
n, m = map(int, input().split())
ma = list(map(int, input().split()))
ma.sort(key= lambda x: (x % 10, x))

ans = 0
for i in ma:
    if m == 0:
        break

    if i % 10 == 0:
        tmp = i // 10 - 1
        if tmp > m:
            ans += m
            tmp = m
        else:
            ans += tmp + 1

    else:
        tmp = i // 10
        if tmp > m:
            ans += m
            tmp = m
        else:
            ans += tmp
    
    m -= tmp
            

print(ans)