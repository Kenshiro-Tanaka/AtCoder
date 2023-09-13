N, X, T = map(int, input().split())

print(N//X*T if N%X==0 else (N//X+1)*T) # N/X*Tだと小数点出ちゃう
