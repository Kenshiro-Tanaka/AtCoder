S = list(map(str, input().split())) # S[0]の方がS[1]より辞書順で小さいと仮定

SS = sorted(S)
print("Yes" if S == SS else "No")
