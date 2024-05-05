N = int(input())
head, sholder = [], []

for _ in range(N):
    A, height = map(int, input().split())
    sholder.append(A)
    head.append(height - A)

ans = 0
head_size = -1
for i in range(N):
    if head_size < head[i]:
        ans += sholder[i]
        head_size = head[i]
    else:
        ans += sholder[i]

print(ans + head_size)