A = int(input())
B = int(input())
C = int(input())
X = int(input())

# 硬貨の中から何枚か選ぶことに注意　全てではない
counter = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500*i + 100*j + 50*k == X:
                counter += 1

print(counter)
