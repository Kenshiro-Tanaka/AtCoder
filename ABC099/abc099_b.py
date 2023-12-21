# 塔の高さは漸化式になっている，n >= 2で a_n = a_1 + sigma(k+1)
tower_h = [1] + [i*(i-1)//2+i for i in range(2, 1000, 1)]

a, b = map(int, input().split())

print(tower_h[b-a-1] - b) # i+1番目の高さはi+1であり，成り立つ式として a+x+i+1 = b+x
