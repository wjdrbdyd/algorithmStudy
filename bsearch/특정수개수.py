from bisect import bisect_left, bisect_right

def count_by_value(arr, x):
  # 데이터 개수
  n = len(arr)
  
  # x가 처음 등장한 인덱스 계산
  a = first(arr, x, 0, n - 1)
  
  #수열에 x가 존재하지 않는 경우
  if a == None:
    return 0

  # x가 마지막으로 등장한 인덱스 계산
  b = last(arr, x, 0, n - 1)
  
  # 개수 반환
  return a - b + 1

# 처음 위치찾는 이진 탐색 메서드 
def first(arr, target, start, end):
  if start > end :
    return None
  mid = (start + end) // 2
  # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
  if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target :
    return mid
  # 중간점의 값 보다 찾고자하는 값이 작거나 같은 경우 왼쪽 확인
  elif arr[mid] >= target:
    return first(arr, target, start, mid - 1)
  # 중간점의 값 보다 찾고자하는 값이 큰 경우 오른쪽 확인
  else :
    return first(arr, target, mid + 1, end)
# 마지막 위치찾는 이진 탐색 메서드 
def last(arr, target, start, end):
  if start > end :
    return None
  mid = (start + end) // 2
  # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
  if (mid == end or target < arr[mid + 1]) and arr[mid] == target :
    return mid
  # 중간점의 값 보다 찾고자하는 값이 작거나 같은 경우 왼쪽 확인
  elif arr[mid] > target:
    return last(arr, target, start, mid - 1)
  # 중간점의 값 보다 찾고자하는 값이 큰 경우 오른쪽 확인
  else :
    return last(arr, target, mid + 1, end)
# def count_by_range(a, left_value, right_value):
#   right_index = bisect_right(a, right_value)
#   left_index = bisect_left(a, left_value)
#   return right_index - left_index

# n, x = map(int, input().split())
# arr = []

# arr= list(map(int, input().split()))
  
# result = count_by_range(arr, x, x)
# if result == 0 :
#   print(-1)
# else :
#   print(result)