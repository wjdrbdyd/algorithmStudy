import time
INF = int(1e9)
# 집의 개수
n = int(input())
house = list(map(int, input().split()))

house.sort()
mid = (len(house) // 2 - 1) if len(house) % 2 == 0 else (len(house) // 2) 
print(house[mid])
## 아이디어 : 중간값에 해당하는 위치의 집에 안테나를 설치했을 때, 안테나로부터 모든 집까지의
## 거리의 총합이 최소가 된다는점. 즉 중간에서 멀어지는 집에 안테나를 설치하면 총합이 계속 증가한다. 


## 내가 푼 방식은 시간초과 뜸 ##
# distance = [INF] * 100001
# # start = time.time()
# for i in range(len(house)):
#   distance[house[i]] = 0
#   for j in range(len(house)):
#     if i == j : 
#       continue
#     distance[house[i]] += abs(house[i] - house[j])
# print(distance.index(min(distance)))
# end = time.time()
# print(f'{end - start: .5f} sec')