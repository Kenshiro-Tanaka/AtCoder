N = int(input())
v = list(map(int, input().split()))

# 毎回小さい2つで処理すると良さそう（貪欲法）
while len(v) != 1:
    sv = sorted(v)
    v = sv[2:] # 先に用いる2つを除いたリストにしておく
    v.append((sv[0]+sv[1])/2)

print(*v)
