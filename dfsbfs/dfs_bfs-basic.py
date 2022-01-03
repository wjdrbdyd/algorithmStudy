# DFS - 깊이 우선 탐색
# 인접 행렬 : 2차원 배열로 그래프의 연결 관계 표현
# INF = int(1e9)
# graph = [
#   [0, 7, 5], 
#   [7, 0 , INF], 
#   [5, INF, 0]
# ]
# # 인접 리스트 : 리스트로 그래프의 연결 관계 표현

# graph = [[] for _ in range(3)]
# graph[0].append((1, 7))
# graph[0].append((2, 5))
# graph[1].append((0, 7))
# graph[2].append((0, 5))

# 두 방식의 차이 #
## 메모리측면 ## 
# -> 인접 행렬 방식은 모든 관계 저장하기 때문에 노드가 많을수록 메모리가 낭비, 
#    인접 리스트는 연결정보만 저장하기 때문에 메모리 효율
## 정보얻는 속도 ##
# -> 인접리스트는 연결된 데이터를 하나씩 확인 해야하므로 느림

##### 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우
# 인접리스트 방식이 인접리스트 방식이 메모리 공간 낭비가 적다.

from collections import deque
# DFS는 특정 경로로 탐색하다 특정 상황에서 최대한 깊숙이 들어가서 노드 방문 후,
# 다시 돌아가 다른 경로 탐색하는 알고리즘
# 스택 자료구조를 이용하며 , 동작 과정
# 1. 탐색 시작 노드를 스택에 삽입하고 방문처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 노드를 스택에 넣고
#    방문 처리, 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드 꺼냄
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복.

def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * len(graph)
# DFS 호출
# dfs(graph, 1, visited)

### BFS - 너비 우선 탐색 가까운 노드부터 탐색하는 알고리즘
# 큐 자료구조 이용 동작 방식
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를
#     모두 큐에 삽입하고 방문 처리
# 3. 2번 과정 더 이상 수행할 수 없을 때까지 반복
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

bfs(graph, 1, visited)




  


