N = int(input())
P = list(map(int, input().split()))

if P == sorted(P): # 最初から昇順の場合
    print("YES")
else:
    a, b = 0, 0 # 昇順ではないところを記憶するa
    for i in range(N-1): # 逆に昇順が一度の入れ替えで崩れているとしたら
        if P[i] > P[i+1]: # P[a]より後ろの最小値とP[a]を入れ替えているはず（y=x描けばすぐ分かる）
            a = i
            break

    b = P.index(min(P[a+1:]))
    P[a], P[b] = P[b], P[a]

    if P == sorted(P):
        print("YES")
    else:
        print("NO")
