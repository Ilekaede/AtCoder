S = input()
T = input()

if T[len(T)-1] == 'X':
    T = T[:-1]
    t = T.lower()
else:
    t = T.lower()

index = 0
cnt = 0
while(index < len(S)):
    # print(cnt, index)
    # print(t[cnt], S[index])
    if t[cnt] == S[index]:
        cnt += 1
    index += 1

    if cnt == len(T):
        break

if(cnt == len(T)):
    print("Yes")
else:
    print("No")