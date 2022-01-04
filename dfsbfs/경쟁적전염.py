from collections import deque
n, k = map(int, input().split())

graph = []
virus = []

for i in range(n):
  graph.append(list(map(int, input().split()))) 
  for j in range(n):
    if graph[i][j] != 0:
      # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
      virus.append((graph[i][j], 0, i, j))
# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
virus.sort()
q = deque(virus)

target_s, target_x, target_y = map(int, input().split())
# 바이러스가 퍼져나갈수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while q:
  v, s, x, y = q.popleft()
  # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
  if s == target_s:
    break
  # 현재 노드에서 주변 4가지 위치를 각각 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 해당 위치로 이동할 수 있는 경우
    if 0 <= nx and nx < n and 0 <= ny and ny < n :
      # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
      if graph[nx][ny] == 0 :
        graph[nx][ny] = v
        q.append((v, s + 1, nx, ny))
print(graph[target_x - 1][target_y - 1])

## 해설은 시간정보 및 바이러스 종류도 튜플로 넣어서 시간관련해서
## 반복문 돌지 않아도됨. 내가 짠건 시간증가에 따라 바이러스를 한번에
## 큐에 넣어 큐를 꺼내면 각 시간에 해당하는 바이러스 묶음이
# 한번에 나와 반복문이 반복문이 훨씬 많이돌게 된다.. 
# 시간 초과 됨.. ... ㅠㅠ 
## 내가 푼거 - 예제 입력은 통과했음. ##
# for i in range(n):
#   graph.append(list(map(int, input().split()))) 
#   for j in range(n):
#     if graph[i][j] != 0:
#       virus.append((i, j))
# s, x, y = map(int, input().split())
# # 상, 하, 좌, 우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# queue = deque([virus])

# for _ in range(s):
#   temp = []
#   while queue:
#   # s초 동안 반복.

#     vi = queue.popleft()
#     # 상, 하, 좌, 우 확인
    
#     for v in vi:
#       i, j = v
#       for z in range(4):
#         nx = dx[z] + i
#         ny = dy[z] + j
        
#         if nx < 0 or nx >= n or ny < 0 or ny >= n:
#           continue
#         if graph[nx][ny] == 0 :
#           graph[nx][ny] = graph[i][j]
#           temp.append((nx, ny))
#   queue.append(temp)

# print(graph[x - 1][y - 1])