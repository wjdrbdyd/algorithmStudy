# 이건 모르겠음.. 문제 많이 풀어보도록 하자.
# 동전 개수 1 <= N <= 1000
n = int(input())
# 동전 종류 나열
data = list(map(int, input().split()))
data.sort()

target = 1

for i in data:
  # 만들 수 없는 금액을 찾았을 때 반복 종료
  if target < i :
    break
  target += i

# 만들 수 없는 금액 출력
print(target)
