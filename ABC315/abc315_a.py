S = input()

ans = []
for i in S:
    if not i in ["a", "e", "i", "o", "u"]:
        ans.append(i)
    
print("".join(ans))
