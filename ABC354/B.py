n = int(input())
sum = 0
list = []
for i in range(n):
    S = input()
    s, c = S.rsplit(maxsplit=1)
    c = int(c)
    sum += c
    list.append(s)

list.sort()
index = sum % n

print(list[index])
