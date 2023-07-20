N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)

print("Yes" if S.count("For") >= len(S) / 2 else "No") # Sの大きさは奇数だからこれでいい
