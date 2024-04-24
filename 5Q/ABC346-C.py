W, B = map(int, input().split())

S = "wbwbwwbwbwbw"
for i in range(len(S)):
    nw = 0
    nb = 0
    for j in range(W+B):
        if S[(i + j) % len(S)]=='w':
            nw += 1
        else:
            nb += 1
    if W == nw and B == nb:
        print('Yes')
        exit(0)
print("No")