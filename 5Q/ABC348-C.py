N = int(input())
dic = {}

for i in range(N):
    A, C = map(int, input().split())
    if(C in dic):
        if dic[C] > A:
            dic[C] = A
    else:
        dic[C] = A

print(max(dic.values()))