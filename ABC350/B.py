N, Q = map(int, input().split())
T = [1] * N
for i in range(N):
    T[i] = 1

t = sum(T)

qs = list(map(int, input().split()))
for q in qs:
        index = q - 1
        # print(index)
        if T[index] == 1:
            T[index] = 0
            t -= 1
        elif T[index] == 0:
            T[index] = 1
            t += 1
        

print(t)