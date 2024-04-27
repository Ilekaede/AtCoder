A = list(map(int, input().split()))
B = list(map(int, input().split()))

sumA = 0
sumB = 0

for i in range(len(A)):
    sumA += A[i]

for i in range(len(B)):
    sumB += B[i]

print(sumA - sumB + 1)