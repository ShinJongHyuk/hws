# Stack을 만든다
stack = []

# stack에 값을 추가한다.
stack.append('A')
print(stack)

# stack에 값을 계속 추가한다.
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')
print(stack)

#stack에서 값을 제거한다
print(stack.pop())
print(stack)

# stack의 가장 마지막 요소를 조회한다.
print(stack[-1])

print(bool(len(stack)))