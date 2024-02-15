N = list(input())
n = [int(i) for i in N]

# 各桁の和を3で割った余りを計算 -> 
# 1だったら余りが1である桁を1つ削るか，2である桁を2つ削るか
# 2だったら余りが2である桁を1つ削るか，1である桁を2つ削るか
surplus = sum(n)%3
surplus_keta = [] # 各桁を3で割った余りを格納
cnt = 0
for i in N:
    surplus_keta.append(int(i)%3)

if surplus == 0:
    print(0)
    exit()
if surplus == 1:
    if 1 in surplus_keta and len(N) >= 2:
        print(1)
        exit()
    elif surplus_keta.count(2)%2 == 0 and len(N) >= 3: # 2桁消すので3桁は必要
        print(2)
        exit()
if surplus == 2:
    if 2 in surplus_keta and len(N) >= 2:
        print(1)
        exit()
    elif surplus_keta.count(1)%2 == 0 and len(N) >= 3: # 2桁消すので3桁は必要
        print(2)
        exit()

print(-1)
