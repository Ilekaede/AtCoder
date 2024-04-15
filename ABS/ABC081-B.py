N = int(input())
A = list(map(int, input().split()))

cnt = 0
while(A.any % 2 == 0):
    cnt = cnt+1
    A.any /= 2

print(cnt)