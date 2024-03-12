x, y = map(int, input().split())

g1 = [1, 3, 5, 7, 8, 10, 12]
g2 = [2]
g3 = [4, 6, 9, 11]
if x in g1 and y in g1:
    print("Yes")
    exit()
if x in g2 and y in g2:
    print("Yes")
    exit()
if x in g3 and y in g3:
    print("Yes")
    exit()
print("No")


# 解説では1から12までの値がどのグループかを保持するリストを用意してgroup[x] == group[y]で判定
# group = [0, 1, 2, 1, 3, 1, 3, 1, 1, 3, 1, 3, 1]
