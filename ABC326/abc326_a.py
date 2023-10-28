X, Y = map(int, input().split())

print("Yes" if 0 < Y-X < 3 or 0 < X-Y < 4 else "No")
