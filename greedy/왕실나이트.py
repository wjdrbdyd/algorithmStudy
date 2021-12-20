
# 현재 나이트 위치 입력 받기
input_data = input()
# x, y = input_data[0] , input_data[1]
col, row = int(ord(input_data[0])) - int(ord('a')) + 1, input_data[1]

count = 0
## 내풀이 ##
# moveX = [-2, -1, 1, 2] 
# moveY = [[-1,1] , [-2,2], [-2,2], [-1,1]]
# 나이트 이동 방향 8가지 

# for i in range(len(moveX)):  
#   nx = ord(col) + moveX[i]

#   for j in range(len(moveY[i])):

#     ny = int(row) + moveY[i][j]

#     if nx < ord('a') or nx > ord('h') or ny < 1 or ny > 8 : 
#       continue 
#     else : 
#       count += 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]
  if next_row >= 1 or next_row <= 8 or next_col >= 1 or next_col <= 8 : 
    count += 1
        
print(count)      
# for a in range(1, 8):
  