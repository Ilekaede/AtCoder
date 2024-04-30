N = int(input())
A = list(map(int, input().split()))
ST = [tuple(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    S, T = ST[i]
    A[i + 1] = (A[i] // S) * T
    print(A[i+1])

print(A[N-1])

