N, M, T = map(int, input().split())
A = list(map(int, input().split()))
bonus = {}
for i in range(M):
    x, y = map(int, input().split())
    bonus[x-1] = y # 考えやすいように部屋のindexを1減らす

for i in range(N-1):
    if T-A[i] <= 0: # 持ち時間が0以下になるような移動はできない
        print("No")
        exit()
    else:
        T -= A[i]
        if i+1 in bonus.keys():
            T += bonus[i+1]
    
print("Yes")
