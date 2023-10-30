N = int(input())

for i in range(N, 920, 1):
    l = list(str(i)) # intからlistはstrを経由する
    tmp = int(l[0])*int(l[1])
    if tmp == int(l[2]):
        break

print(i)
