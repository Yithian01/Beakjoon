import sys
input = sys.stdin.readline

n = int(input())
INF = n + 1

vi = [False] * INF
q = []

# 소수 리스트 생성
for i in range(2, INF):
    if vi[i]:
        continue
    q.append(i)
    for j in range(i * i, INF, i):
        vi[j] = True

st, ed = -1, len(q) - 1  # 왼쪽 끝과 오른쪽 끝 설정

while st + 1 < ed:  # 열린 구간 ( ]
    mid = (st + ed) // 2
    tmp = q[mid]

    print(f"? {tmp}")
    sys.stdout.flush()  # 출력한 내용을 즉시 전달
    m = int(input())
    
    if m == 0:  # 존재하지 않음
        ed = mid  # F일 경우, ed를 mid로 설정
    else:  # 존재함
        st = mid  # T일 경우, st를 mid로 설정

print(f"! {q[ed]}")  # 가장 왼쪽의 F에 해당하는 소수를 출력
sys.stdout.flush()
