N, K = map(int, input().split())

if N%K == 0: # 好きな回数行えるから0に到達するなら0 -> 割り切れたら0
    print(0)
else:
    cnt = N//K
    N -= cnt*K # できるだけ近づいた状態
    tmp = abs(N-K)
    print(min(tmp, N))

# ABC175 C問題の方が少し複雑
    
