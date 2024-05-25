n, t = map(int, input().split())
a = list(map(int, input().split()))
dict = {}
for i in range(n * n):
    dict[i + 1] = False

for i in range(n):
    print("aho")
for i in range(t):
    dict[i] = True
