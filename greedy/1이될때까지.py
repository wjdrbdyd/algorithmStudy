# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행. 
# 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택 가능
  # 1. N에서 1을 뺀다.
  # 2. N을 K로 나눈다.
# 옐ㄹ 들어 N이 17, K가 4라고 가정. 1번 수행 N ← 16, 이후 2번 과정 두 번 수행하면 N ← 1
# 전체 과정 실행 횟수 3 , N을 1로 만드는 최소 횟수

n, k = map(int, input().split())

result = 0 
# 내 풀이 
# while True:
#   if n == 1 : 
#     break
#   if n % k == 0 : # 2번 수행
#     n = n / k
#     result += 1
#   else :          # 1번 수행
#     n -= 1  
#     result += 1

# N이 K 이상이라면 K로 계속 나누기   - 나누기 해야 n이 빨리 감소한다 라는 아이디어 
# 1. n이 커지면 오래걸림
# while n >= k :
#   # N이 K로 나누어 떨어지지 않으면 1 뺌
#   while n % k != 0 :
#     n -= 1
#     result += 1
#   # k로 나누기
#   n = n // k
#   result += 1

# # 마지막 남은 수에 대하여 1씩 뺌
# while n > 1 :
#   n -= 1
#   result += 1
# 2. n이 k의 배수가 되도록 효율적으로 한번에 빼는 방식
while True:
  # (n == k로 나누어떨어지는 수)가 될 때까지 1씩  빼기
  target = (n // k) * k 
  # res = n % k  # 나머지 
  result += (n - target)
  # result = res
  n = target
  # n = n - res
  # n이 k보다 작을 때 ( 더 이상 나눌 수 없을 때 ) 반복문 탈출
  if n < k :
    break
  # k로 나누기
  result += 1
  n //= k
# 마지막으로 남은 수에대하여 1씩 빼기 (한번에)
result += (n-1)
print(result)