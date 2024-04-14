S = input()
s = {}

for char in S:
    if char in s:
        s[char] += 1
    else:
        s[char] = 1

cntMax = -1
minAlpha = None
for char in s:
    if s[char] > cntMax or (s[char]==cntMax and (minAlpha is None or char < minAlpha)):
        cntMax = s[char]
        minAlpha = char

print(minAlpha)