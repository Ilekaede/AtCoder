S = input()
s = set()
for i in range(len(S)):
    for j in range(1, len(S) - i + 1):
        substring = S[i:i+j]
        s.add(substring)

print(len(s))
