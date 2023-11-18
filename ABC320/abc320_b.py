S = list(input())

for i in range(len(S)): # 回文が見つからなかったら窓を小さくする
    # 窓を横にスライドしていくイメージ
    for j in range(i+1): # 対象とする部分文字列の開始位置を制御
        n = len(S)-i # 窓の長さ
        if S[j:n+j] == list(reversed(S[j:n+j])):
            print(len(S[j:n+j]))
            exit()
