# 1. 국어 점수 내림차순
# 2. 영어 점수 오름차순
# 3. 수학 점수 내림차순
# 4. 이름 오름차순 대문자는 소문자앞
n = int(input())
arr = []
for i in range(n):
  arr.append(input().split())

print(arr)
arr.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]) ,x[0] ))

for a in arr:
  print(a[0])

  