N = input()

# 0をつけていくのではなく外して考えたい
N = N.rstrip("0") # 便利すぎ

N = list(N)
n = list(reversed(N)) # 反転したやつと一致していなかったら終了
for i in range(len(N)):
    if N[i] != n[i]:
        print("No")
        exit()

print("Yes")
