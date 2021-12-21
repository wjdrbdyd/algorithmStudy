

##  집합 자료형 풀이 ##
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x :
  if i in array :
    print('yes', end=' ')
  else :
    print('no', end=' ')
## 계수 정렬 풀이 ##
# n = int(input())
# array = [0] * 1000001
# for i in input().split():
#   array[int(i)] = 1

# m = int(input())
# x = list(map(int, input().split()))

# for i in x :
#   if array[i] == 1:
#     print('yes', end=' ')
#   else :
#     print('no', end=' ')
## 이진 탐색으로 풀이 ##
# n = int(input())
# data1 = list(map(int, input().split()))  # 부품
# m = int(input())
# data2 = list(map(int, input().split()))  # 찾을 부품
# def binary_search(array, target, start, end):
#   while start <= end :
#     mid = (start + end) // 2
#     if array[mid] == target :
#       return mid
#     elif array[mid] > target:
#       end = mid - 1
#     else :
#       start = mid + 1
#   return None
    
# data1.sort()

# for target in data2:
#   result = binary_search(data1, target, 0, n-1)
#   if result == None:
#     print('no', end=' ')
#   else :
#     print('yes', end=' ')
