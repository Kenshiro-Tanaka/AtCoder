L, R = list(map(int,input().split()))
S = input()

s = S[L-1:R] # 反転部分を抽出
print(S[:L-1]+s[::-1]+S[R:]) # 反転して挿入
