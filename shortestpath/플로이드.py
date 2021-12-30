INF = int(1e9)
# 도시 개수(노드)
n = int(input())
# 버스 개수(간선)
m = int(input())
# 2차원 리스트(그래프)를 만들고, 모든 값을 무한으로 초기화 
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신에서 자기 자신으로 가는 비용 0 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b :
      graph[a][b] = 0

arr = [[] for _ in range(m + 1)]
  
for i in range(m):
  # A에서 B로 가는 비용 C
  a, b, c = map(int, input().split())
  # arr[a].append((b, c))                 내가 짠 부분
  # 가장 짧은 간선 정보만 저장
  if c < graph[a][b]:
    graph[a][b] = c 

# 가장 짧은 간선 정보만 저장
# for i in range(1, n + 1):               내가 짠 부분 
#   now = arr[i]
#   for dis in now:
#     b, c = dis
#     graph[i][b] = min(graph[i][b], c)
    
# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if graph[i][j] == INF :
      graph[i][j] = 0
    print(graph[i][j], end=' ')
  print()