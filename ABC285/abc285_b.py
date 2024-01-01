N = int(input())
S = input()

# 一致しないでどこまでいけるか
# わかりにくい問題文なのでテストケースから考えた
for i in range(1, N, 1): # i は飛ばす数
    k = 0
    while k+i < N:
        if S[k] == S[k+i]:
            break
        k += 1
    print(k)
