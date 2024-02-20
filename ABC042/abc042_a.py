l = list(map(int, input().split()))

print("YES" if l == [5, 7, 5] or l == [5, 5, 7] or l == [7, 5, 5] else "NO")
