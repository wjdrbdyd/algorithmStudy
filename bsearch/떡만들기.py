# 첫 줄 떡 개수 N, 떡 길이 M
# 둘째 줄 떡 개별 높이 떡 높이 총합은 항상 M 이상



n, m = map(int, input().split())
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)  # 떡 최대 길이

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in array:
    # 잘랐을 때의 떡양 계산
    if x > mid :
      total += x - mid
  # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
  if total < m :
    end = mid - 1
  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else :
    result = mid # 최대한 덜 잘랐을 때가 정답이므로 , result에 기록
    start = mid + 1

print(result)
## 내 풀이 - 문제점 어마어마한 큰 수 들어오면 시간초과 될듯? ##
# h = max(array) - 1 # 가장 큰 값 

# while True:
#   sum = 0
#   for i in array :
#     if i - h > 0 :
#       sum += i - h
#   if sum >= m :
#     print(h)
#     break
#   else :
#     h = h - 1  
      