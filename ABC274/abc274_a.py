A, B = map(int, input().split())

print(str(round(B / A, 3)).ljust(5, '0')) # 右に0埋め
