import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)] # iからjに行くのにかかる時間がT[i][j]

cnt = 0
# 始点は決まっているので(N-1)!通り試せばいい，列挙を簡単にするためにitertoolsを使う
for root in itertools.permutations(range(1, N, 1)): # 始点は0で確定なので1からでいい
    pos, time = 0, 0
    
    for i in range(N-1):
        time += T[pos][root[i]] # root内の隣の要素に行くのにかかる時間
        pos = root[i]

    time += T[pos][0] # 終点から都市0に戻る分を足す
    
    if time == K:
        cnt += 1
    
print(cnt)
