from collections import deque
n, m = map(int, input().split())
graph = []

for i in range(1, n + 1):
  graph.append(list(map(int, input())))
# 상 하 좌 우 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
  # 큐에 처음 시작 추가
  queue = deque([(a, b)])
  # 큐가 빌 때까지 반복
  while queue:
    # 현재 위치 꺼내서 
    x, y = queue.popleft()
    # 현재 위치에서 상하 좌우 탐색
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue
      if graph[nx][ny] == 0 : 
        continue
      # 해당 노드를 처음 방문하는 경우만 최단 거리 기록
      # graph[nx][ny] != 0 인걸로 조건 걸었기 때문에 무한루프 빠짐.
      # 상하 좌우 0이아닌거 계속 상하좌우 탐색하며 큐에 추가하게 된다.
      # 조건 생각을 잘못했다.
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[n - 1][m - 1]
    
print(bfs(1, 1))
