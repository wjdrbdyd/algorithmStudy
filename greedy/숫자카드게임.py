# 룰을 지키며 가장 큰 숫자 뽑기 
# 1. 숫자가 쓰인 카드들이  N x M 형태. 이때 N은 행의 개수, M은 열의 개수
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행 선택.
# 3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드 뽑음.
# 4. 처음에 카드를 골라낼 행 선택할 때, 이후 해당 행에서 가장 숫자가 낮은 카드를 뽑을걸
#     고려하여 최종적으로 가장 높은 숫자 카드 뽑을 수 있도록 전략 세워야 함

n, m  = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은수 찾기 
  # min_value = min(data)
  min_value = 10001
  for a in data :
    min_value = min(min_value, a)
  # 가장 작은 수 들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)