# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어스 / 스테이지에 도달한 플레이어수
# n <= 1, stages 각 값은 n + 1 이하 자연수
# n + 1은 마지막스테이지(n번째 스테이지) 까지 클리어한 사용자
# 스테이지에 도달한 유저 없는 경우 해당 스테이지 실패율 0


def solution(n, stages):
  answer = []
  length = len(stages)
  
  for i in range(1, n + 1):
    
    # 해당 스테이지에 머물러 있는 사람 수 계산
    count = stages.count(i)
    # 실패율
    if length == 0 :
      fail = 0
    else :
      fail = count / length
    
    answer.append((i, fail))
    length = length - count
  # 각 단계별 실패율 계산
  answer = sorted(answer, key=lambda t: t[1], reverse=True)
  answer = [i[0] for i in answer]
  return answer
## 내가 푼거 - 리뷰 : 코드만 다를뿐 논리는 맞는데 뭐가 문제인지 ... ##  
# def solution(n, stages):
#   answer = []
#   length = len(stages)
#   failure = [0] * (n + 1)   #스테이지에 도달한 사람수 담을 배열
#   # 해당 스테이지에 머물러 있는 사람 수 계산
#   for i in range(1, length + 1):
#     if stages[i - 1] == n + 1:
#       failure[stages[i - 1] - 1] = 0
#     else :
#       failure[stages[i - 1]] += 1
#   # 각 단계별 실패율 계산
#   for i in range(1, n + 1):
#     if length == 0 :
#       fail = 0
#     else :
#       fail = failure[i] / length
#     answer.append((i, fail))
#     length -= failure[i] 
#   answer = sorted(answer, key=lambda t: t[1], reverse=True)
#   answer = [i[0] for i in answer]
#   return answer

# result = solution(5, [6,6, 2, 1, 4, 2, 1, 2, 1, 2, 6, 2, 4, 3, 3])
# print(result)
# result = solution(4, [4, 4, 4, 4, 4])
# print(result)  