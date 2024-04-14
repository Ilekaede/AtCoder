Q = int(input())
A = []

for i in range(Q):
    q, num = map(int, input().split())
    if q == 1:
        A.append(num)
    elif q == 2:
        print(A[len(A) - num])
