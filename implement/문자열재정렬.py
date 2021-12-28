import time
s = input()
strArr = []
numArr =[]
start = time.time()
value = 0
# 내 풀이 아스키코드 값을 이용해 문자인지 숫자를 판단 했다.
for i in s :
  if ord(i) >= 48 and ord(i) <= 57 :
    numArr.append(int(i))
  else :
    strArr.append(i)

# 해설은 파이썬 함수 isalpha() 사용하여 쉽게 구현함.
# for i in s :
#   if i.isalpha():
#     strArr.append(i)
#   else :
#     value += int(i)
strArr.sort()
# if value != 0 :
#   strArr.append(str(value))
result = ''.join(strArr)
value = sum(numArr)
if value != 0 :
  result.append(str(value))
end = time.time()
print(result)  
print(f'{end - start: .5f} sec')