# 팀, 연산 개수
n, m = map(int, input().split())

parent = [0] * (n + 1)  # 루트 ~~!!

# 부모 테이블상, 부모를 자기 자신으로 초기화
for i in range(n + 1):
  parent[i] = i

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

result = []
for _ in range(m):
  c, a, b = map(int, input().split())

  if c == 1 :
    if find_parent(parent, a) == find_parent(parent, b):
      result.append('YES')
    else :
      result.append('NO')
  else :
    union_parent(parent, a, b)

for i in result :
  print(i)
