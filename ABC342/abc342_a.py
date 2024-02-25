S = input()

l = list(set(S))
if S.count(l[0]) == 1:
    print(1)
else:
    print(S.index(l[1])+1)
    
