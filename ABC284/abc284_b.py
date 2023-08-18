T = int(input())
ans = []
for _ in range(T):
    int(input()) # N使わないので
    A = list(map(int, input().split()))
    cnt = 0
    for i in A:
        if i % 2 != 0:
            cnt += 1
    ans.append(cnt)

for i in ans:
    print(i)

# ansに入れずに逐一出力しようとしたら変になるのは1000000000が大きいからか
