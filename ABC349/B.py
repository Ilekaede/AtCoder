S = input()
alphabets = {}
for char in S:
    if char in alphabets:
        alphabets[char] += 1
    else:
        alphabets[char] = 1

frequently_count = {}
for count in alphabets.values():
    if count in frequently_count:
        frequently_count[count] += 1
    else:
        frequently_count[count] = 1

flag = True
for freq, i in frequently_count.items():
    if i != 0 and i != 2:
        flag = False
        break

if flag :
    print("Yes")
else:
    print("No")