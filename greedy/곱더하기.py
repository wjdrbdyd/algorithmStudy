# 곱하기 혹은 더하기
# s의 길이가 20으로 제한됨. s를 반복문으로 돌려 각 게산결과를 
# result 배열에 저장 마지막 계산 결과를 출력하면 됨
# 결과값이 0이거나 1일 때 혹은 해당 문자 값이 0이거나 1일 때
# 덧셈 그 외 곱셈
# 해설에 두 수에 대하여 연산을 수행할 때, 두 수중에서 하나라도 1 이하인 경우에는 더하며,
# 두수가 모두 2이상인경우에는 곱하면 된다라고 나와있음. 
s = input()
s = [int(i) for i in s]

# 배열로 할 필요없이 그냥 결과값 더해서 나타내면 되는거였음
# result = [0] * len(s)
result = int(s[0])

for i in range(1, len(s)):
  # 두 수 중에서 하나라도 0 혹은 1인 경우 곱하기보다 더하기 수행
  if result <= 1 or s[i] <= 1 :  
    result += s[i]
  else :
    result *= s[i]
  # if result[i - 1] <= 1 or s[i] <= 1:
  #   result[i] = s[i] + result[i - 1]
  # else :
  #   result[i] = s[i] * result[i - 1]

print(result)