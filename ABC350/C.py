N = int(input())
A = list(map(int, input().split()))
cnt = 0


for i in range(N):
    for j = i+1 in range(N - 1):
        if(A[i] > A[j]):
            print(A[j], A[i])
            temp = A[i]
            A[j] = A[i]
            A[i] = temp
            cnt += 1



