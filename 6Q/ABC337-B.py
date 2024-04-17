S = input()
# A = []
# B = []
# C = []

i = 0
while(S[i] == 'A'):
    if len(S) - 1 == i:
        i += 1
        break
    else:
        i += 1

if i != len(S):
    while(S[i] == 'B'):
        if len(S) - 1 == i:
            i += 1
            break
        else:
            i += 1

if i != len(S):

    while(S[i] == 'C'):
        if len(S) - 1 == i:
            i += 1
            break
        else:
            i += 1

if i == len(S):
    print("Yes")
else:
    print("No")
