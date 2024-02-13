N = int(input())
S = input()

# ランレングス圧縮をして各文字の最大連続数を出して合計すればいい
alphabet26 = [0]*26 # alphabet26[1]にはbの最大連続数が入るといった風に
l = 0
while l < N:
    r = l+1
    while r < N and S[l] == S[r]:
        r += 1
    c = ord(S[l]) - ord("a")
    alphabet26[c] = max(alphabet26[c], r-l)
    l = r
    
print(sum(alphabet26))
