def ReLU(x):
    return (x if x >= 0 else 0)

x = int(input())

print(ReLU(x))
