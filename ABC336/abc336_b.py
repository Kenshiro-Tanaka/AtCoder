X = bin(int(input()))

ctz = 0
X = str(X)
for i in range(len(X)):
    if X[-(i+1)] == "0": # 文字としての0と等しいかであることに注意
        ctz += 1
    else:
        print(ctz)
        exit()
