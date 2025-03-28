import sys
from heapq import heappush, heappop
input = sys.stdin.readline

'''
    1 p x = p일에 x 추가 
    2 p q = p ~ q일 까지 변화한 양 출력 

    문제만 읽었을 때에는 누적합인 것 같다.
    그런데 heap도 사용해야 할 것 같다. 모든 입력 다받고 하는 것이 아닌 것 같다.
    
    2가 등장하면 그전까지 1을 가지고 해야 하는 것 같다.
    * 실시간 누적합 가능? <- 이거 불가능 하면 O(Q^2) = 10^10

    
    - 세그트리 찾는 로직 
        [st ~ ed] 를 찾는 것 
        st % 2 == 1이라는 것은 왼쪽이므로 st만 필요하다.
        st % 2 == 0 이면 st가 오른쪽이므로 부모 노드가 필요 
        
        ed 는 반대
        ed % 2 == 0이면 왼쪽으므로 현재 ed만 필요 
        ed % 2 ==1 이면 오른쪽이므로 부모가 필요 

        - 그럼 만약에 st, ed 가 3,4 처럼 겹치면 어떡하나요?
            그럴 일이 없다 그런일이 발생한다면 그 부모 노드만 ans에 넣어진다.

'''
def search(st, ed):
    ans = 0
    while st <= ed:
        
        if st % 2 == 1:
            ans += tree[st]
            st +=1
        
        if ed % 2 == 0:
            ans += tree[ed]
            ed -= 1
        
        st >>= 1 
        ed >>= 1
    
    return ans



tree = [0] * (1 << 21)

bios = 1 << 20
n, m = map(int, input().split())

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        b += bios
        while b:
            tree[b] += c
            b >>= 1
        
    else:
        b += bios
        c += bios
        print(search(b, c))