stack = []
for token in input().split():
    if token.isdigit():
        stack.append(int(token))
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
        if token == '+':
            stack.append(operand1 + operand2)
        elif token == '-':
            stack.append(operand1 - operand2)
        elif token == '*':
            stack.append(operand1 * operand2)
print(stack.pop())
