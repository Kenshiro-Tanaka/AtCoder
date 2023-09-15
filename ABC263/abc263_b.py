N = int(input())
P = list(map(int, input().split()))

cnt = 0
tmp = N
while tmp != 1:
    tmp = P[N-2] # 子
    N = P[N-2] # 親を次のループで子にするため
    cnt += 1

print(cnt)

# 26 入力例
# 0                                                        26-2 番目
# 1 2 3 2 1 1 1 8 4 7   6 1 3 3 2 6 17 13 6 15    20 2 8 24 17  入力例
# P[26-2] -> P[17-2] -> P[6-2]      親
#    26   ->    17   ->    6   -> 1 子
