n = int(input())
g = list(map(int, input().split()))
g.sort()

# 접근 법은 비슷했으나 문제를 제대로 읽지 않았음.
# 몇명의 모험가가 마을에 그대로 남아도 된다는점. !!! 유의하자 
result = 0
count = 0 # 현재 그룹에 포함된 모험가의 수
for i in g :
  count += 1
  if count >= i :
    result += 1
    count = 0

print(result)
  