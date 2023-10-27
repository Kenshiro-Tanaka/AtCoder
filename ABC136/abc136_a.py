A, B, C = map(int, input().split())

print(max(C-(A-B),0)) # 全部の水を移せる場合C-(A-B)は負になる
