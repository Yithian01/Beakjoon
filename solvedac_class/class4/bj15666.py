#처음에 set을 이용해서 중복을 제거한뒤 원래 개수가 되면 문자열로 바꾸어서 출력해준다.
#
#시간 복잡도 계산 : n log n + n^M => O(n^m) => 8^8 > 2^24 
#                                                ㄴ> 2^10 => 10^3 
#                                                    2^20 => 10^6 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = sorted(set(list(map(int, input().split()))))


ans = []
q = []
def bt(cnt, idx):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(idx, len(ma)):
        ans.append(ma[i])
        bt(cnt + 1, i)
        ans.pop()

    
bt(0,0)