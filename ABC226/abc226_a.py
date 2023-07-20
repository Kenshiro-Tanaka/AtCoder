X = float(input())

print(int((X * 10) // 10) if 0 <= (X * 10) % 10 < 5 else int(((X * 10) // 10) + 1))
# round(X)とすると0.5が0になるため，Xに十分小さい正数を加える必要がある
