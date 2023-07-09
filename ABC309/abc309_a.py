A, B = map(int, input().split())

print("No" if A % 3 == 0 else "Yes" if B - A == 1 else "No")
