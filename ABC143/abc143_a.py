A, B = map(int, input().split())

print(max(A-2*B, 0)) # 完全に覆う以上のカーテンがあったら値は0以下になってしまう
