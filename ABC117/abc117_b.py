N = int(input())
L = list(map(int, input().split()))

m = max(L)
L.remove(m)
print("Yes" if m < sum(L) else "No")
