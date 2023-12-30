X, A, B = map(int, input().split())

print("delicious" if A >= B  else "safe" if A+X >= B else "dangerous") # 買った日を基準にして，Bに対して3通りの場合分け
