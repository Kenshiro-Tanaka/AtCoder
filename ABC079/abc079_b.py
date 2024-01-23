l = [2, 1] # リュカ数リストを作るなら85回のループで済む
for i in range(2, 87, 1):
    l.append(l[i-1]+l[i-2])

N = int(input())

print(l[N])


# 再帰呼び出しだとすごく時間がかかる
# def Lucas(i):
#     if i == 0:
#         return 2
#     elif i == 1:
#         return 1
#     else:
#         return Lucas(i-1)+Lucas(i-2)
