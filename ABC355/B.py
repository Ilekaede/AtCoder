from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
atp = []
for i in range(n):
    atp.append((a[i], "a"))
b = list(map(int, input().split()))
btp = []
for i in range(m):
    btp.append((b[i], "b"))

ctp = atp + btp
ctp.sort()

# print(ctp)
Flag = True

for i in range(0, len(ctp) - 1):
    p1 = ctp[i][1]
    p2 = ctp[i+1][1]
    if p1 == "a" and p2 == "a":
        Flag = False
        break

if Flag:
    print("No")
else:
    print("Yes")

