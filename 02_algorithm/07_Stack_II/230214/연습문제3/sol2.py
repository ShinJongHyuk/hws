import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    print(start, end= ' ')

    # 다음 조사 가능 위치 칮기
    for next in range(1, V+1):
        # 인접해 있고, 방문한 적 없는 곳
        if G[start][next] and not visited[next]:
            # 조사를 한다는 행위
            DFS(next)



# V = voltex = 노드
# E = Edge = 간선

V, E = map(int, input().split())
data = list(map(int,input().split()))

# 이동 가능 정보를 담기 위한 리스트
# 0번 노드는 쓰지 않고, V번 노드도 필요하므로 V+1

G = [[0]*(V+1) for _ in range(V+1)]

# 인접 행렬 그리기
for i in range(E): # 간선의 개수 만큼 그리기
    # 두개의 노드가 이어져 있는 정보
    n1, n2 = data[i*2], data[i*2 +1]
    G[n1][n2] = 1 # n1에서 n2로 갈 수 있다.
    G[n2][n1] = 1 # 양방향으로 이동 가능하므로

# for i in range(0, len(data), 2):
#     print(data[i], data[i+1])

for mat in G:
    print(mat)

# 방문 표시용 배열 생성
visited = [0] * (V+1)
DFS(1)