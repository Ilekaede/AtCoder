N, K = map(int, input().split())
A = list(map(int, input().split()))
st = set()
for i in range(N):
    set.add(A[i])

sum = (1 + K) * K / 2
for _ in range(N):
    n = st.pop()
    if n <= K:
        sum -= A[i]
print(int(sum))