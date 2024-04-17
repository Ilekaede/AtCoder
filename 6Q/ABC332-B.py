K, G, M = map(int, input().split())
g = 0
m = 0
while(K > 0):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        while(m != 0):
            m -= 1
            g += 1
            if(g == G):
                break
    K -= 1
print(g, m)