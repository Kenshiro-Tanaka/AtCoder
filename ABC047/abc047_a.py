l = list(map(int, input().split()))

l = sorted(l)
print("Yes" if l[0] + l[1] == l[2] else "No")
