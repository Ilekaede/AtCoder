A = int(input()) # 500
B = int(input()) # 100
C = int(input()) # 50
X = int(input()) # 金額

cnt = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500 * i + 100 * j + 50 * k == X:
                cnt = cnt + 1

print(cnt)