N, D = map(int, input().split())

i = 1 # 人数
while((2*D+1)*i < N): # 1人で見れる範囲は2D+1
    i += 1

print(i)
