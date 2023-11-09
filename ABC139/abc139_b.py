A, B = map(int, input().split())

n = 1 # コンセントの空いている数
tap = 0
while(n < B):
    n += A-1
    tap += 1

print(tap)
