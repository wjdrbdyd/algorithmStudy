# 파이썬에서 스택을 이용할 때에는 기본리스트에서 append, pop 이용하면 스택동작
stack = []

# 삽입 5, 2, 3, 7 , 삭제 , 삽입 1, 4, 삭제 
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
# 5, 2, 3, 1
print(stack[::-1])  # 최상단 원소부터 출력

# 파이썬으로 큐를 구현할 때 collection 모듈 deque 이용
from collections import deque
queue = deque()
# 삽입 5, 2, 3, 7 , 삭제 , 삽입 1, 4, 삭제 
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
print(queue)  # 먼저 들어온 순서대로 출력 -> 3, 7, 1, 4
