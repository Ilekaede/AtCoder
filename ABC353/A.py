N = int(input())
H = list(map(int, input().split()))

index = 1
for i in range(len(H)):
    if H[index] < H[i]:
        index = i
if index == 0:
    print(-1)
else:
    print(index)