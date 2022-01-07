import heapq
# 핵심아이디어 : 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해 보장
n = int(input())
# heap에 초기카드 묶음 모두 삽입
heap = []
for i in range(n):
  data = int(input())
  heapq.heappush(heap, data)
result = 0

while len(heap) != 1:
  # 가장 작은 2개의 카드 묶음 꺼내기
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  # 카드 묶음 합쳐서 다시 삽입
  sum_value = one + two
  result += sum_value
  heapq.heappush(heap, sum_value)
print(heapq.heappop)
print(result)