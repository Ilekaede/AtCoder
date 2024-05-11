N, K = map(int, input().split())
A = list(map(int, input().split()))
empty_chair = K;

cnt = 0
index = 0
while(index < N):
    if A[index] > empty_chair:
        cnt += 1
        empty_chair = K
    else:
        empty_chair -= A[index]
        index += 1

print(cnt + 1)