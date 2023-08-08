N = int(input())
P = list(map(int, input().split()))

if max(P) != P[0]: # 人1が最強ではない
    print(max(P) - P[0] + 1)
else: # 人1は最強のうちの1人
    # 人1以外にも最強がいるかどうか
    print(1 if len(P) > 1 and max(P) == max(P[1:]) else 0) # max(P[1:])はlen(P)>=2じゃないとエラー
