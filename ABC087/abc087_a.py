X = int(input())
A = int(input())
B = int(input())

tmp = X - A # 最初からtmp円だとして考える
print(tmp - tmp//B*B)
