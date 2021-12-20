# 큰 수의 법칙 p.92
# N, M, K
n, m, k = map(int, input().split()) 
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

# 1. 가장 큰수를 k번 더하고 두번째 큰수 1번 더한다.
# 나의 풀이 
# count = 0
# for i in range(m):
#   if count < k :
#     result += first
#     count += 1
#   else :
#     result += second
#     count = 0

# 가장 큰수 더해지는 횟수
count = (m // (k+1)) * k
count += m % (k+1)

result += count * first 
result += (m - count) * second 

print(result)
