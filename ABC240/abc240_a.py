a, b = list(map(int, (input().split())))

print("Yes" if abs(a - b) == 9 or abs(a - b) == 1 else "No")
