import sys
input = sys.stdin.readline


ma = [[0], [3, 9, 7],  [8] ,[1, 7, 9],  [6], [0], [4], [1, 3, 9],[2],[1, 3, 7] ]
isGO = [[0], [2, 5, 4],  [5] ,[2, 5, 6],  [5], [0], [5], [4, 5, 8],[5],[5, 6, 8] ]


n = int(input())
q = list(map(int, input().split()))
vi = [0] * 10
vi[q[0]] = 1
for i in range(1, n):
    isCheck = False

    # 해당 넘버로 이동할 때 불가능한 경우에 
    # 지나가는 곳이 이미 vi활성화 되있으면 그냥 갈 수 있다.
  
    for j in range( len(ma[q[i-1]])):
        if ma[q[i-1]][j] == q[i] and vi[ isGO[q[i-1]][j] ] <= 0:
            isCheck = True    

    if isCheck or vi[q[i]] >= 1:
        print('NO')
        break

    vi[q[i]] += 1


else:
    print('YES')