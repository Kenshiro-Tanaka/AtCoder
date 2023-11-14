A, B, C = map(int, input().split())

print(min(B//A, C)) # 最大B//A回だけどCを超えたらCで良いからmin()
