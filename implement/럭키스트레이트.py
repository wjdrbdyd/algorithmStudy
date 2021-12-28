import time

n = input()
length = len(n) # 정수값의 총 자릿수
summary = 0

start = time.time()
# 왼쪽 부분 자릿수 합 더하기
# for i in range(length // 2):
#   summary += int(n[i])

# for i in range(length // 2, length):
#   summary -= int(n[i])
  
# if summary == 0:
#   print('LUCKY')
# else :
#   print('READY')
# 내 풀이 법 시간이 오래걸리려나 ?   
n = [int(i) for i in n]

left = sum(n[0 : len(n) // 2])
right = sum(n[len(n) // 2 :])
print(f'left:{left}, right:{right}')
if left == right:
  print('LUCKY')
else :
  print('READY')
end = time.time()
print(f'{end - start: .5f} sec')

  