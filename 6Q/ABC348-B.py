import math
N = int(input())
X = []
Y = []
for i in range(N):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

for i in range(N):
    ans = -1
    maxDis = -1
    for j in range(N):
        dis = math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
        if(dis > maxDis):
            ans = j+1
            maxDis = dis
    print(ans)
