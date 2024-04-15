N, A, B = map(int, input().split())

someSums = 0
for i in range(A+1):
    for j in range(B+1):
        sum = i * 10 + j
        if sum < N:
            break
        else:
            print(sum)
            someSums += sum

print(someSums)

