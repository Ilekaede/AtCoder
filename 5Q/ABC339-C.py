N = int(input())
A = list(map(int, input().split()))

sum = 0
for i in range(len(A)):
    sum += A[i]
    if sum < 0:
        sum += -(sum)

print(sum)