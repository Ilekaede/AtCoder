h = int(input())

flag = True
i = 0
vHeight = 0
while(flag):
    vHeight += 2 ** i
    if h - vHeight < 0:
        flag = False
    else:
        i += 1
print(i + 1)