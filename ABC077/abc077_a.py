C1 = input()
C2 = input()

tmp = ""
for i in range(len(C1)):
    tmp += C1[len(C1)-1-i]

print("YES" if tmp == C2 else "NO")
