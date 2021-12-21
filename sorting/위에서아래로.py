# n = int(input())
# arr = []
# for i in range(n):
#   arr.append(int(input()))  
  
# arr = sorted(arr, reverse=True)
# for i in arr :

n = int(input())
array = []
for i in range(n):
  m = input().split()
  m[1] = int(m[1])
  array.append((m[0], m[1]))

array = sorted(array, key=lambda student: student[1])
for student in array :
  print(student[0], end=' ')
  

