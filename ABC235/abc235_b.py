N = int(input())
H = list(map(int, input().split()))

pos = 0 # positionは横移動
for _ in range(N):
    if pos != N - 1 and H[pos] < H[pos + 1]: # 判定時点のposの最大はN-2
        pos += 1

print(H[pos])
