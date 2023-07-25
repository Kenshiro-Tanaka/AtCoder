S = input()

idx = 0
for i in range(len(S)):
    if S[i] == 'a':
        idx = i
        
print(idx + 1 if 'a' in S else -1) # indexとは1ずれる
