# from itertools import combinations
# # 내가 푼 방법 조합 combination 이용해서 a b 무게가 같지 않을때만 카운트 
n, m = map(int, input().split())
data = list(map(int, input().split()))
# 1부터 10까지 무게를 담을 수 있는 리스트
array = [0] * 11
for i in data:
  array[i] += 1
result = 0
for i in range(1, m + 1):
  n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  result += array[i] * n   # B가 선택하는 경우의 수와 곱하기 
  # a가 선택하는 경우의 수 * b가 선택하는 경우의 수
  # result += array[i] * sum(array[i + 1:m + 1]) 

# count = 0
# for i in combinations(data, 2):
#   a, b = i
#   if a != b :
#     count += 1


# print(count)
print(result)