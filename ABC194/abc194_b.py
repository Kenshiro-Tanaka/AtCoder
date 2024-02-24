import itertools

N = int(input())
l, s = [], []
for _ in range(N):
    a, b = map(int, input().split())
    l.append((a, b))
    s.append(a+b) # 同じ人に割り当てる場合

tmp = 10**5
for pair in itertools.permutations(l, 2):
    v = max(pair[0][0], pair[1][1]) # 2人の従業員にそれぞれA,Bを割り当てた時のかかる時間を全て出した
    tmp = min(tmp, v)

print(min(tmp, min(s))) # 同じ人に割り当てて小さいこともある
