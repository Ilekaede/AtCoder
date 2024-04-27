N = int(input())
A = list(map(int, input().split()))

stack = []

for i in range(N):
    stack.append(A[i])
    flag = True
    while(flag):
        if len(stack) == 1:
            flag = False
            continue
        elif len(stack) > 1:
            a1 = stack.pop()
            a2 = stack.pop()
            if a1 != a2:
                stack.append(a2)
                stack.append(a1)
                flag = False
            else:
                stack.append(a1 + 1)

print(len(stack))