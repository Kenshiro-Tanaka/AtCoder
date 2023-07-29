a, b = map(int, input().split())

# すごい悩んだけどA問題だから法則だろうなと思った
print("Yes" if b == a * 2 or b == a * 2 + 1 else "No")
# a == b//2　でいい
