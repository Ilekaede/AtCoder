n = int(input())
card = []
for i in range(n):
    a,c = map(int, input().split())
    card.append(((a,c),i))

card.sort(reverse=True)

cBase = card[0][0][1]
# print("cbase", cBase)
ansList = []

for i in range(n):
    a,c = card[i][0][0], card[i][0][1]
    if i == 0:
        ansList.append(card[i])
        continue

    if c > cBase:
        continue
    else:
        ansList.append(card[i])
        cBase = c

ansList.sort(key=lambda x:x[1])

print(len(ansList))

outPut = " ".join(str(i[1]+1) for i in ansList)
print(outPut)