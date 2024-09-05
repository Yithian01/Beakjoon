# post의 마지막 배열은 root node가 확정이다.
# 그럼 inorder에서 그 위치를 찾고 le, ri로 나눠준다.
# inorder의 le의 크기를 찾는다.
# post의 0 + le - 1인 곳은 다시 inorder의 root가 확정이 된다.

# 1 3 4 5 6 7 12 15 16
# 1 4 6 5 3 12 16 15 7

# (1) 7이 root확정
# (2) 7의 idx = 5
# (3) 왼쪽의 크기 => 5 - 0 = 5 
# (4) post에서 왼쪽의 크기 -1 idx = 3임 
# (5) 3 은 다음 왼쪽 최상위 root확정임
# (6) 3의 idx = 1 
# (7) 왼쪽의 크기 => 1 - 0 = 1 
# (8) 1은 다음 왼쪽 확정 
# (9) 1의 idx = 0 
# (10) 왼쪽의 크기 => 0 
# (11) idx가 0보다 작아졌으므로 빠져나오기 

# 오른쪽 역시 같은 동작 

# 시간 복잡도 계산: O(N log N) => 10^5 * 18 => 10^6정도
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[inOrder[i]] = i

#남은노드 시작   끝   , post 시작, 끝
def sol(in_st, in_ed, po_st, po_ed):
    if (in_st > in_ed) or (po_st > po_ed):
        return 
    
    root = postOrder[po_ed]
    print(root, end= ' ')
    po = pos[root]

    le = po - in_st # 왼쪽의 크기 
    ri = in_ed - po # 오른쪽의 크기 

    # post의 왼쪽 다음 root는 inorder의 왼쪽 끝 index 찾는것 
    sol(in_st, in_st + le -1, po_st, po_st + le -1)
    # post의 오른쪽 다음 root는 inorder의 오른쪽 끝 index 찾는것 
    sol(in_ed - ri + 1, in_ed, po_ed - ri, po_ed -1)

sol(0, n-1, 0, n-1)