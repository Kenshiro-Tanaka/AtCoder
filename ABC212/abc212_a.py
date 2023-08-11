A, B = map(int, input().split())

print("Gold" if (0 < A and B == 0) else "Silver" if (A == 0 and 0 < B) else "Alloy")
