N = int(input())
A = list(map(int, input().split()))
aSum = 0
for i in range(N): # 全部の和
    aSum += A[i]

x = 10 ** 8

sum = 0
aSub = 0
for i in range(N - 1):
    aSub += A[i];
    print(A[i] * (N - (i+1)) + aSum - aSub)
    sum += (A[i] * (N - (i+1)) + aSum - aSub) % x
    
print(int(sum))