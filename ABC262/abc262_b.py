N, M = map(int, input().split())
# 隣接リストを作る
graph = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1) # 有向グラフなら消す

cnt = 0
for i in range(N):
    for j in range(i+1, N, 1):
        for k in range(j+1, N, 1):
            if j in graph[i] and k in graph[j] and i in graph[k]:
                cnt += 1

print(cnt)        
