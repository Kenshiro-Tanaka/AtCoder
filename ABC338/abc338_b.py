S = input()

l = [0]*26
for i in range(26):
    l[i] = S.count(chr(97+i))

print(chr(97+l.index(max(l))))
