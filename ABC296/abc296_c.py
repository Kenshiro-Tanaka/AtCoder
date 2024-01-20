N, X = map(int, input().split())
A = set(list(map(int, input().split()))) # N^2で回すと間に合わないからsetで

for i in A:
    if i+X in A:
        print("Yes")
        exit()

print("No")
