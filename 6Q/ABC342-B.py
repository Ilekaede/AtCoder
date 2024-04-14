
N = int(input())
P = list(map(int, input().split()))

Q = {}
for i in range(N):
    Q[P[i]] = i

q = int(input())

for _ in range(q):
    Q[P[i]] = i
    A, B = map(int, input().split())

    if(Q[A] < Q[B]):
        print(A)
    else:
        print(B)

