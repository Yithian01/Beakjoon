import sys
input = sys.stdin.readline
# 1) 해당 버블 정렬 로직은 인덱스가 최악의 경우 한번에 하나씩만 이동한다.
# 2) 정렬 전 인덱스를 딕셔너리에 key: val로 넣어준다.
# 3) python 정렬 함수를 이용해 N Log N 으로 정렬 완료 후 
# 가장 차이가 큰 인덱스 차를 출력 \

# 이거 10 10 3 10 10 와 같이 숫자가 동일한 경우에도 봐주어야 하기 때문에 새로운 배열을 만드는 것이 유리 
# 또한 가장 버블 정렬은 가장 n - i번째에 큰수를 확정짓기 때문에 0번째 idx에서 마지막 idx로 가야하는 경우 1의 횟수만 든다.
# 50 3 4 5 6 같은 경우 4인줄 알았지만 1번의 횟수로 가능함 ( 버블 정렬이기에 )

# 즉 이전 idx - sortIdx 가 양수인 경우 
# 3 4 5 6 1 같은 경우만 취급해주어야 한다.

# 시간 복잡도 계산 : N + N Log N + N => 10^7정도로 통과 가능


n = int(input())
ma = list(map(int, input().split()))

ta = {}
for idx, val in enumerate(ma):
    ta[val] = idx

ma.sort()
ans = 0

sortTa = {}
for idx, val in enumerate(ma):
    sortTa[val] = idx

for i in ma:
    tmp = ta[i] - sortTa[i]
    if tmp > 0:
        ans = max(ans, tmp)

print(ans)