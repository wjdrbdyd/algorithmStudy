# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  
  if a < b :
    parent[b] = a
  else :
    parent[a] = b
  
# 노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1)

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
  parent[i] = i

# 간선 정보 입력 받기
for _ in range(m):
  a, b, c = map(int, input().split())
  # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((c, a, b))
  
# 간선을 비용순 정렬
edges.sort()
last = 0    # 가장 큰 간선 (정렬 했기 때문에 마지막추가되는게 가장 큼)
# 간선을 하나씩 확인
for edge in edges:
  c, a, b = edge
  # 같은 루트를 갖지 않는다면 경로에 추가
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += c
    last = c


print(result - last)